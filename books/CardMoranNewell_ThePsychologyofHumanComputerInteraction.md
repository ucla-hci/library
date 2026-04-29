# 1. An Applied Information-Processing Psychology

### Main focus of this book

> The domain of concern to us, and the subject of this book, is how humans interact with computers. A scientific psychology should help us in arranging this interface so it is easy, efficient, error-free—even enjoyable.
> 

### On the persistent style of HCI

> Whatever continued evolution the interface takes—and it will be substantial—human-computer interaction is unlikely ever to lose this character of a conversational dialogue.
> 

### Users operating vs. communicating with computers

> But the user is not an operator. He does not operate the computer, he communicates with it to accomplish a task. Thus, we are creating a new arena of human action: communication *****with***** machines rather than operation *****of***** machines.
> 

### Elements of applied psychology on human-computer interaction

- Task analysis: what are the individual tasks a user needs to perform;
- Calculation: “… how long would it take people to do present physical tasks …”;
- Approximation: it is necessary to simplify calculation given the complex human nature;

### On why task analysis is related to psychology

> … humans behave in a goal-oriented way. … they attempt to adapt to the task environment to attain their goals. Once the goals are known or can be assumed, the structure of the task environment provides a large amount of the predictive content of psychology.
> 

### On statistical significance and effect size

> The neglect of approximation has been especially encouraged by the emphasis on statistical significance rather than on the magnitude of an effect. A difference of a few percent in performance at two levels of an independent variable is usually of little practical importance and can often be ignored in an approximation, even if the difference is highly significant statistically.
> 

### On whether one should apply psychology on evaluation or on design

> In design, one wants results expressed explicitly as a function of some controllable parameters, in order to explore optimization and sensitivity. In evaluation, this urge is much diminished; experimental evaluation is so expensive as to be prohibitive, permitting exploration of only two or three levels of each independent variable. Most importantly, by the time a system is running well enough to evaluate, it is almost inevitably too late to change it much. Thus, an applied psychology aimed exclusively at evaluation is doomed to have little impact.
> 

### On application vs. theory

> Ultimately, as a theory becomes solidified, application areas contribute less and less to the basic science. But at the beginning, just the reverse is true.
> 

### On the role of HCI in CS

> When university curriculum committees draw up a list of “what every computer scientist should know to call himself a computer scientist,” we think models of the human user have a place alongside models of compilers and language interpreters.
> 

### What can HCI do for CS?

> The yield for computer science that can flow from an applied psychology of human-computer interaction is engineering methods for taking the properties of users into account during system design.
>

# 2. The Human Information-Processor

### Human the information processor

> Modern cognitive psychology had come a long way in understanding man as a processor of information.
> 

### Caveat of the “model”

> The description is approximate when applied to the human, intended to help us remember facts and predict user-computer interaction rather than intended as a statement of what is really in the head.
> 

### The three subsystems of the Model Human Processor

> (1) the perceptual system, (2) the motor system, and (3) the cognitive system
> 

### Important parameters of the Model Human Processor

For memory

> $\mu$: the storage capacity in items
$\delta$: the decay time of an item, and
$\kappa$: the main code type (physical, acoustic, visual, semantic)
> 

For processor

> $\tau$: the cycle time
> 

> … there is no separate parameter for access time in this model since it is included in the processor cycle time.
> 

### Principles of operation for the Model Human Processor

(x[y-z] means a typical number is x and lower bound y and upper bound z—based on measurement in literature)

<aside>
💡 ****************************************************************************************************P0. Recognize-Act Cycle of the Cognitive Processor****************************************************************************************************
On each cycle of the Cognitive Processor, the contents of Working Memory initiate actions associatively linked to them in Long-Term Memory; these actions in turn modify the contents of Working Memory.

</aside>

<aside>
💡 **************************************************************************************************P1. Variable Perceptual Processor Rate Principle**************************************************************************************************
The Perceptual Processor cycle time $\tau_P$ varies inversely with stimulus intensity.

</aside>

<aside>
💡 ********************************************************************P2. Encoding Specificity Principle********************************************************************
Specific encoding operations performed on what is perceived determine what is stored, and what is stored determines what retrieval cues are effective in providing access to what is stored.

</aside>

<aside>
💡 **********************************************************P3. Discrimination Principle**********************************************************
The difficulty of memory retrieval is determined by the candidates that exist in the memory, relative to the retrieval clues.

</aside>

<aside>
💡 **********************************************************************************************P4. Variable Cognitive Processor Rate Principle**********************************************************************************************
The Cognitive Processor cycle time $\tau_C$ is shorter when greater effort is induced by increased task demands or information loads; it also diminishes with practice.

</aside>

<aside>
💡 ******P5. Fitts’s law******
The time $T_\text{pos}$ to move the hand to a target of size $S$ which lies a distance $D$ away is given by 
$T_\text{pos} = I_M \log_2(D/S + .5)$
where $I_M = 100 [70-120]\text{msec/bit}$

</aside>

<aside>
💡 **********************************************************P6. Power Law of Practice**********************************************************
The time $T_n$ to perform a task on the $n$th trial follows a power law:
$T_n = T_1n^{-\alpha}$
where $\alpha = .4[.2-.6]$

</aside>

<aside>
💡 **P7. Uncertainty Principle**
Decision time $T$ increases with uncertainty about the judgement or decision to be made:
$T = I_CH$
where $H$  is the information-theoretic entropy of the decision and $I_C = 150[0-157]\text{msec/bit}$. For $n$ equally probable alternatives (called **Hick’s Law**),
$H = \log_2(n+1)$
For $n$ alternatives with different probabilities, $p_i$, of occurences,
$H = \sum_ip_i\log_2(1/p_i + 1)$

</aside>

<aside>
💡 **P8. Rationality Principle**
A person acts so as to attain his goals through rational action, given the structure of the task and his inputs of information and bounded by limitations on his knowledge and processing ability:
Goals + Task + Operations + Inputs + Knowledge + Process-limits $\rightarrow$ Behavior

</aside>

<aside>
💡 ************************************************************P9. Problem Space Principle************************************************************
The rational activity in which people engage to solve a problem can be described in terms of (1) a set of states of knowledge, (2) operators for changing one state into another, (3) constraints on applying operators, and (4) control knowledge for deciding which operator to apply next.

</aside>

### Head movements and gaze

> Whenever the target is more than about 30 degrees away from the fovea, head movements occur to reduce the angular distance. These four parts—central vision, peripheral vision, eye movements, and head movements—operate as an integrated system, largely automatically, to provide a continual representation of the visual scene of interest to the perceiver.
> 

### Visual perception cycle

$$
\tau_P = 100[50-200]\text{msec}
$$

> If a stimulus impinges upon the retina at time $t = 0$, at the end of time  $t = \tau_p$ the image is available in the Visual Image Store and the human claims to see it.
> 

### Human’s effectors

> For computer users, the two most important sets of effectors are the arm-hand-finger system and the head-eye system.
> 

### Chunks and its retrieval

> The activated elements of Long-Term Memory, which define Working Memory, consist of symbols, called ******chunks******, which may themselves be organized into larger units.
> 

> There are two reasons the attempt to retrieve a chunk might fail: (1) effective retrieval associations cannot be found, or (2) similar associations to several chunks interfere with the retrieval of the target chunk.
> 

### Recall

> When people are asked to recall information a few seconds after hearing it, they use both Working Memory and Long-Term Memory to do so.
> 

### Writing to long-term memory

> Items cannot be added to Long-Term Memory directly; rather, items in Working Memory (possibly consisting of several chunks) have a certain probability of being retrievable later from Long-Term Memory.
> 

### The recognize-act cycle

> On each cycle, the contents of Working Memory initiate associatively-linked actions in Long-Term Memory (”recognize”), which in turn modify the contents of Working Memory (”act”), setting the stage for the next cycle.
> 

> The cognitive system is fundamentally parallel in its recognizing phase and fundamentally serial in its action phase. Thus the cognitive system can be aware of many things, but cannot do more than one deliberate thing at a time.
>