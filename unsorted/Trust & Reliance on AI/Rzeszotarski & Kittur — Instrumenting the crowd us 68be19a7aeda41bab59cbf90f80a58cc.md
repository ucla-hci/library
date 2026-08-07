# Rzeszotarski & Kittur — Instrumenting the crowd: using implicit behavioral measures to predict task performance

```

@inproceedings{rzeszotarski_instrumenting_2011,
	address = {New York, NY, USA},
	series = {{UIST} '11},
	title = {Instrumenting the crowd: using implicit behavioral measures to predict task performance},
	isbn = {978-1-4503-0716-1},
	shorttitle = {Instrumenting the crowd},
	url = {https://doi.org/10.1145/2047196.2047199},
	doi = {10.1145/2047196.2047199},
	abstract = {Detecting and correcting low quality submissions in crowdsourcing tasks is an important challenge. Prior work has primarily focused on worker outcomes or reputation, using approaches such as agreement across workers or with a gold standard to evaluate quality. We propose an alternative and complementary technique that focuses on the way workers work rather than the products they produce. Our technique captures behavioral traces from online crowd workers and uses them to predict outcome measures such quality, errors, and the likelihood of cheating. We evaluate the effectiveness of the approach across three contexts including classification, generation, and comprehension tasks. The results indicate that we can build predictive models of task performance based on behavioral traces alone, and that these models generalize to related tasks. Finally, we discuss limitations and extensions of the approach.},
	urldate = {2024-07-12},
	booktitle = {Proceedings of the 24th annual {ACM} symposium on {User} interface software and technology},
	publisher = {Association for Computing Machinery},
	author = {Rzeszotarski, Jeffrey M. and Kittur, Aniket},
	month = oct,
	year = {2011},
	pages = {13--22},
}

```

# One Sentence

---

This paper presents a method that predicts the quality of crowdworkers’ tasks based on “task fingerprinting”—behavior traces of the crowdworkers as they complete a task, such as how they scroll, clicks, and type on the task page.

# More Sentences

---

# Key Points

---

### What is “behavioral traces”

> In their raw form, they are sequential logs of interface events; what the workers did, and when.
> 

### Useful technical details related to logging

Chunking behaviors into 200-px windows

> … sequences of scrolling and mouse movement encoded into individual events for each 200 pixels total moved or scrolled
> 

Adding a special “delay” event:

> … if a user waits longer than a specific time threshold (here we use 200 milliseconds) a delay event is encoded, with further delay events added for every 200 milliseconds the user waits
> 

Behavior of entering in text fields, which can be analogous to typing in the prompt

> … the cumulative time they spent before they started typing in a form field, and the cumulative time they spent between keystrokes in a form field.
> 

# Other Notes

---

# Take-Away

---

### How such (quality) detection can be used

> … we could identify workers that ignore the guidelines of one task so that we could flag all of their work across all tasks for closer examination
> 

Similarly, we can set up a threshold to flag overreliance behavior, which then will turn on intervention mechanisms.

### Opportunities for visualization

> Visualization of the fingerprints might enable human outlier and pattern detection in large sets of workers.
> 

We might provide users with visualization of their behaviors (even without detection) to promote their awareness of overreliance

### User event logging

This is not a new approach. Already lots of work reviewed by this 2011 paper. Need to sample more recent ones.

### Building on this paper

- The writing can follow what this paper does
- We can start with what this paper logs, report how they work; then add our own (new) behavior logs.

### Formulating the detection/prediction problem into multiple levels

- Binary classification (over- or proper reliance)
- Multi-class classification (e.g., no, mild, medium, severe overreliance)
- Regression, i.e., the degree of overreliance in a numeric value

### Crowdworkers seem to have every incentive to overrely on LLM …

The bright side: data collected can contain various degrees of overreliance

Bad: population skewed, not representative of the general user groups