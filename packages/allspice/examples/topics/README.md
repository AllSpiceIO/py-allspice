# Examples: Using topics

This directory has two example scripts. The first, `clone_all_repos_by_topic.py`
will let you clone every repo from an instance that has a certain topic
associated with it. The second, `add_topic_to_repos.py` will take a YAML file
as input and add topics to all the repos as defined in the YAML.

## Clone all repos

To run the script, run the following command:

```bash
python3 clone_all_repos_by_topic.py -h
```

This should generate help text that tells you how to use the script.

## Add topics to repos

This script takes a YAML file as input. The YAML file has the following pattern:

```yaml
topic1:
    - "owner1/repo1"
    - "owner1/repo2"
    - "owner2/repo1"
topic2:
    - "owner1/repo3"
    - "owner2/repo2"
```

When run with this yaml file as input, the script will add `topic1` as a topic
to the three repos under it, and `topic2` as a topic to the two repos under it.

For help on how to run the script, start with:

```bash
python3 add_topics_to_repos.py -h
```
