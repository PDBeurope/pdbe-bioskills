from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from pdbe_bioskills.discovery import discover_all
from pdbe_bioskills.installer import (
    install_agent_claude,
    install_agent_codex,
    install_skill_claude,
    install_skill_codex,
)

app = typer.Typer(
    name="pdbe-bioskills",
    help="Install agent skills and agent profiles for PDBe analyses or workflows.",
    no_args_is_help=True,
)

console = Console()


@app.command("list")
def cmd_list() -> None:
    """List all available skills and agents."""
    items = discover_all()
    if not items:
        console.print("[yellow]No skills or agents found.[/yellow]")
        raise typer.Exit(1)

    table = Table(title="pdbe-bioskills", show_header=True, header_style="bold")
    table.add_column("Type", style="cyan", width=8)
    table.add_column("Name", style="bold")
    table.add_column("Description")
    for item in items:
        table.add_row(item.kind, item.name, item.description)
    console.print(table)


@app.command("install")
def cmd_install(
    names: Optional[list[str]] = typer.Argument(default=None, help="Names of items to install"),
    all_items: bool = typer.Option(False, "--all", help="Install everything"),
    claude: bool = typer.Option(False, "--claude", help="Target Claude Code (.claude/)"),
    codex: bool = typer.Option(False, "--codex", help="Target Codex (.codex/)"),
    # `global` is a Python keyword — typer maps the --global flag to global_ parameter
    global_: bool = typer.Option(False, "--global", help="Install to $HOME instead of current directory"),
    directory: Optional[Path] = typer.Option(None, "--dir", help="Custom install base directory"),
) -> None:
    """Install skills and/or agent profiles into your project."""
    items = discover_all()
    if not items:
        console.print("[red]No skills or agents found in package.[/red]")
        raise typer.Exit(1)

    # Resolve base directory
    if directory is not None:
        base = directory.resolve()
    elif global_:
        base = Path.home()
    else:
        base = Path.cwd()

    # Resolve targets
    if not claude and not codex:
        choice = typer.prompt(
            "\nInstall for?\n  [1] Claude Code\n  [2] Codex\n  [3] Both\nChoice",
            default="1",
        )
        if choice == "2":
            codex = True
        elif choice == "3":
            claude = True
            codex = True
        else:
            claude = True

    # Resolve item selection
    if all_items:
        selected = items
    elif names:
        name_set = set(names)
        selected = [i for i in items if i.name in name_set]
        missing = name_set - {i.name for i in selected}
        for m in sorted(missing):
            console.print(f"[yellow]Warning:[/yellow] '{m}' not found — skipping.")
    else:
        # Interactive numbered menu
        console.print("\n[bold]Select items to install:[/bold]")
        last_kind = ""
        for idx, item in enumerate(items, start=1):
            if item.kind != last_kind:
                console.print(f"\n  [cyan]{item.kind.capitalize()}s:[/cyan]")
                last_kind = item.kind
            console.print(f"    [{idx}] [bold]{item.name}[/bold] — {item.description}")

        raw = typer.prompt("\nEnter numbers separated by spaces, or 'all'")
        if raw.strip().lower() == "all":
            selected = items
        else:
            selected = []
            for token in raw.split():
                try:
                    n = int(token)
                    if 1 <= n <= len(items):
                        selected.append(items[n - 1])
                except ValueError:
                    pass

    if not selected:
        console.print("[yellow]Nothing selected.[/yellow]")
        raise typer.Exit(0)

    console.print(f"\n[bold]Installing to {base}[/bold]")
    for item in selected:
        if item.kind == "skill":
            if claude:
                dest = install_skill_claude(item, base)
                console.print(f"  [green]✓[/green]  skill  [bold]{item.name}[/bold] → {dest}")
            if codex:
                dest = install_skill_codex(item, base)
                console.print(f"  [green]✓[/green]  skill  [bold]{item.name}[/bold] → {dest}/")
        else:
            if claude:
                dest = install_agent_claude(item, base)
                console.print(f"  [green]✓[/green]  agent  [bold]{item.name}[/bold] → {dest}")
            if codex:
                dest = install_agent_codex(item, base)
                console.print(f"  [green]✓[/green]  agent  [bold]{item.name}[/bold] → {dest}")

    console.print("\n[green]Done.[/green]")
