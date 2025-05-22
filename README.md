# VMVT Epidemic Simulator

A Python-based epidemic simulator that integrates **biological mechanisms** and **individual behavior** to model the spread of infectious diseases.  
This work is part of the Master’s Thesis:


## 🧠 Model Summary

The simulator is based on a **P system with active membranes**, merging the biological realism of **LOIMOS** with the behavioral modeling of **MVT**.

It adopts an extended **SEJIRS** epidemiological model:

- **S**: Susceptible
- **E**: Exposed (infected, not yet infectious)
- **J3**: Moderately symptomatic (isolated, hospitalized if needed)
- **J4**: Severely symptomatic (ICU, high risk of death)
- **I**: Infected and infectious
- **R**: Recovered (temporary immunity)

### Key Features:
- Probabilistic infection and symptom development
- Behavioral parameters: prudence, vaccination, inter-province mobility
- Hospitalization, ICU management, and quarantine modeling
- Graphical interface to configure and run simulations
- Output as both CSV data and visual plots

---

## 🚀 Installation

To install and run the simulator:

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/sejirs-simulator.git
cd sejirs-simulator
```

2. **(Optional) Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required Python packages**

```bash
pip install -r requirements.txt
```

> If not working, install the required packages manually (e.g., `tkinter`, `matplotlib`, `pandas`, etc.)

---

## ▶️ Running the Simulation

To launch the simulator, run:

```bash
python interface.py
```

- This will open a GUI where you can configure simulation parameters.
- Start the simulation from the interface.
- The simulation will run and generate output automatically.

---

## 📁 Simulation Output

After the **first simulation**, a new folder called `simulation/` will be created:

```
simulation/
├── results.csv         # Raw output with time-series data
└── graphs/             # Graphs and visualizations of the simulation
```

### What You’ll Find:
- `results.csv`: contains daily stats (infected, exposed, recovered, deaths, etc.)
- `graphs/`: includes PNG plots for:
    - Infection and recovery trends
    - Symptom progression
    - Behavioral impact (e.g., prudence, vaccination)
    - Province movement effects

---
## 📚 Related Work

- **LOIMOS**: *P systems in the time of COVID-19*
- **MVT**: *A dynamic behavior epidemiological model by membrane systems*

This simulator combines both to create a flexible, generalized model for research and experimentation in epidemic simulations.
