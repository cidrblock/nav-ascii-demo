import subprocess

from .defs import Act
from .images import images

base = [
    Act(command="clear"),
    Act(command="rm demo.json"),
    Act(command="asciinema rec demo.json -y", sleep=2),
    Act(command="ansible-navigator --demo --osc4 false", sleep=2),
]

end =[
    Act(command=":quit", sleep=1),
    Act(command="exit")
]

commands = [
    "xdotool selectwindow",
    "xdotool type 'clear'",
    "xdotool key Return",
]

def main():
    acts = base + images + end

    for act in acts:
        line = []
        if act.command:
            commands.append(f"xdotool type '{act.command}'")
            commands.append("sleep 1")
            commands.append("xdotool key Return")
        elif act.key:
            commands.append(f"xdotool key {act.key}")
        commands.append(f"sleep {act.sleep}")


    subprocess.check_output("\n".join(commands), shell=True)


if __name__ == "__main__":
    main()
