# Subruotines
setup(){
  if [ ! -d venv ]; then
    echo "Creating virtual environment"
    python -m venv venv
  fi
  echo "Loading virtual environment"
  source venv/bin/activate
  echo "Installing dependencies"
  pip install -r requirements.txt
}

start(){
  echo "Loading virtual environment"
  source venv/bin/activate
  echo "Running app"
  python -m app
}

print_help(){
  echo "$0 [-h] <command>"
  echo ""
  echo "command"
  echo "  help     muestra este mensaje de ayuda"
  echo "  start    levanta la aplicación"
  echo "  setup    prepara el entorno virtual e instala las dependencias"
}

# Main
command="$1"

case "${command}" in
  setup)
    setup
    ;;
  start)
    start
    ;;
  help|"")
    print_help
    ;;
  *)
    echo "Comando desconocido: ${command}"
    print_help
    ;;


esac



