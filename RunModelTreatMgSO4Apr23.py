import ParameterClassesApr23 as P
import MarkovModelApr23 as MarkovCls
import SupportMarkovModelApr23 as SupportMarkov
import scr as PathCls
import scr as Figs

# create and simulate cohort
cohort = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.MGSO4)

simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of number of strokes
Figs.graph_histogram(
    data=simOutputs.get_if_developed_stroke(),
    title='Number of Strokes per Patient',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)

# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs, 'Treatment:')
