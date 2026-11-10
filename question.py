def get_questions():
    questions = [
        {
            "question": "What is the primary responsibility of a teacher?",
            "options": {
                "A": "To facilitate learning",
                "B": "To punish students",
                "C": "To give homework every day",
                "D": "To control students"
            },
            "answer": "A"
        },
        {
            "question": "What should a teacher do when a student struggles to understand a topic?",
            "options": {
                "A": "Ignore the student",
                "B": "Explain the topic using another approach",
                "C": "Punish the student",
                "D": "Move to another topic immediately"
            },
            "answer": "B"
        },
        {
            "question": "Why is classroom management important?",
            "options": {
                "A": "To make students afraid",
                "B": "To reduce teaching time",
                "C": "To create an organised learning environment",
                "D": "To prevent students from asking questions"
            },
            "answer": "C"
        },
        {
            "question": "What is the best way to encourage student participation?",
            "options": {
                "A": "Discourage questions",
                "B": "Allow only the best students to speak",
                "C": "Ignore students' opinions",
                "D": "Create opportunities for everyone to contribute"
            },
            "answer": "D"
        },
        {
            "question": "What should a teacher do before introducing a new topic?",
            "options": {
                "A": "Prepare a lesson plan",
                "B": "Start teaching without preparation",
                "C": "Give students an examination",
                "D": "Dismiss the class"
            },
            "answer": "A"
        },
        {
            "question": "What is the purpose of a lesson plan?",
            "options": {
                "A": "To punish students",
                "B": "To guide teaching and learning activities",
                "C": "To replace classroom teaching",
                "D": "To reduce student participation"
            },
            "answer": "B"
        },
        {
            "question": "How should a teacher handle a disruptive student?",
            "options": {
                "A": "Shout at the student immediately",
                "B": "Ignore every disruption",
                "C": "Address the behaviour calmly and fairly",
                "D": "Send the student home immediately"
            },
            "answer": "C"
        },
        {
            "question": "What does continuous assessment help a teacher understand?",
            "options": {
                "A": "The teacher's popularity",
                "B": "The number of students in school",
                "C": "The students' favourite subjects",
                "D": "Students' learning progress over time"
            },
            "answer": "D"
        },
        {
            "question": "What should a teacher do when preparing teaching materials?",
            "options": {
                "A": "Choose materials relevant to the lesson objectives",
                "B": "Use materials without checking them",
                "C": "Avoid visual materials completely",
                "D": "Use the same materials for every topic"
            },
            "answer": "A"
        },
        {
            "question": "Why should teachers give students feedback?",
            "options": {
                "A": "To embarrass students",
                "B": "To help students understand their strengths and areas for improvement",
                "C": "To discourage learning",
                "D": "To compare students publicly"
            },
            "answer": "B"
        },
        {
            "question": "What should a teacher do if two students are having a disagreement?",
            "options": {
                "A": "Automatically support one student",
                "B": "Ignore the disagreement",
                "C": "Listen to both sides and address the issue fairly",
                "D": "Punish both students without investigation"
            },
            "answer": "C"
        },
        {
            "question": "What is differentiated instruction?",
            "options": {
                "A": "Teaching every student in exactly the same way",
                "B": "Allowing only advanced students to participate",
                "C": "Teaching without lesson objectives",
                "D": "Adapting teaching methods to meet different learning needs"
            },
            "answer": "D"
        },
        {
            "question": "Why is punctuality important for a teacher?",
            "options": {
                "A": "It demonstrates responsibility and professionalism",
                "B": "It allows teachers to avoid lessons",
                "C": "It reduces the need for preparation",
                "D": "It gives teachers fewer responsibilities"
            },
            "answer": "A"
        },
        {
            "question": "What should a teacher do when a student asks a question they cannot answer?",
            "options": {
                "A": "Give an incorrect answer",
                "B": "Admit they need to verify the answer and follow up",
                "C": "Embarrass the student",
                "D": "Ignore the question"
            },
            "answer": "B"
        },
        {
            "question": "What is the main purpose of classroom rules?",
            "options": {
                "A": "To make students afraid",
                "B": "To prevent all discussions",
                "C": "To establish clear expectations for behaviour",
                "D": "To remove student independence"
            },
            "answer": "C"
        },
        {
            "question": "How can a teacher support a student with learning difficulties?",
            "options": {
                "A": "Exclude the student from activities",
                "B": "Assume the student cannot improve",
                "C": "Ignore the student's needs",
                "D": "Provide appropriate support and learning adjustments"
            },
            "answer": "D"
        },
        {
            "question": "What is the purpose of an examination?",
            "options": {
                "A": "To assess students' knowledge and understanding",
                "B": "To make students afraid of school",
                "C": "To replace every classroom activity",
                "D": "To punish students for mistakes"
            },
            "answer": "A"
        },
        {
            "question": "What should a teacher do to maintain students' attention?",
            "options": {
                "A": "Speak continuously without interaction",
                "B": "Use engaging teaching methods and activities",
                "C": "Avoid explaining difficult concepts",
                "D": "Discourage student participation"
            },
            "answer": "B"
        },
        {
            "question": "Why should teachers maintain confidentiality about students' personal information?",
            "options": {
                "A": "To avoid communicating with parents",
                "B": "To hide students' academic progress",
                "C": "To protect students' privacy",
                "D": "To prevent students from receiving support"
            },
            "answer": "C"
        },
        {
            "question": "What should a teacher do after completing a lesson?",
            "options": {
                "A": "Forget the lesson immediately",
                "B": "Avoid checking students' understanding",
                "C": "Move on without reviewing progress",
                "D": "Evaluate the lesson and identify areas for improvement"
            },
            "answer": "D"
        },
        {
            "question": "What is the importance of communication between teachers and parents?",
            "options": {
                "A": "It supports students' learning and development",
                "B": "It allows parents to control every classroom activity",
                "C": "It removes the teacher's responsibilities",
                "D": "It prevents students from becoming independent"
            },
            "answer": "A"
        },
        {
            "question": "What should a teacher do when students have different learning speeds?",
            "options": {
                "A": "Ignore slower learners",
                "B": "Provide appropriate support while maintaining learning objectives",
                "C": "Teach only the fastest learners",
                "D": "Stop giving challenging activities"
            },
            "answer": "B"
        },
        {
            "question": "What does inclusive education mean?",
            "options": {
                "A": "Teaching only students without disabilities",
                "B": "Separating students based on their abilities",
                "C": "Providing learning opportunities for students with diverse needs",
                "D": "Allowing only high-performing students into classrooms"
            },
            "answer": "C"
        },
        {
            "question": "What should a teacher do if they notice a student is being bullied?",
            "options": {
                "A": "Ignore the situation",
                "B": "Blame the student being bullied",
                "C": "Encourage students to handle it alone",
                "D": "Follow safeguarding procedures and report the incident appropriately"
            },
            "answer": "D"
        },
        {
            "question": "Why should teachers continue developing their professional skills?",
            "options": {
                "A": "To improve their teaching knowledge and effectiveness",
                "B": "To avoid learning new teaching methods",
                "C": "To reduce their classroom responsibilities",
                "D": "To avoid receiving feedback"
            },
            "answer": "A"
        }
    ]
    return questions