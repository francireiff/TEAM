from simulation import Simulation

def main():
    # Inizializza una simulazione
    simulation = Simulation()

    # Crea uno scenario
    simulation.create_scenario()
    print("Starting the simulation from colab_main")

    # Esegui la simulazione per 5 giorni
    simulation.run_simulation(days=40)

if __name__ == "__main__":
    main()