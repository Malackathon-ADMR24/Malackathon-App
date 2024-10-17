set -e

# Subruotines
source secrets/secrets.sh

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
  local environment="$1"
  local configfile="configuration.$environment.yml"

  echo "Loading virtual environment"
  source venv/bin/activate
  echo "Running app ($environment)"
  python -m app "$configfile"
}

sync(){
  rsync -av -e "ssh -i ${PRIVATE_KEY}" --exclude-from='.rsyncignore' . "${SERVER_USER}@${SERVER_HOST}:${REMOTE_APP_DIR}"
}

deploy(){
  ssh -i ${PRIVATE_KEY} "${SERVER_USER}@${SERVER_HOST}" 'pid=`sudo lsof -i:80 | grep python | grep LISTEN | awk '"'"'{print $2}'"'"'`;sudo kill $pid'
  sync
  ssh -i ${PRIVATE_KEY} "${SERVER_USER}@${SERVER_HOST}" "cd ${REMOTE_APP_DIR};( sudo ./run.sh start_pro )& disown"
}

print_help(){
  echo "$0 [-h] <command>"
  echo ""
  echo "command"
  echo "  deploy   copia el proyecto al servidor remoto"
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
    start dev
    ;;
  start_pro)
    start pro
    ;;
  deploy)
    deploy
    ;;
  sync)
    sync
    ;;
  help|"")
    print_help
    ;;
  *)
    echo "Comando desconocido: ${command}"
    print_help
    ;;


esac



