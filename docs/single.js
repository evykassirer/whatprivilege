var questionNo = 0;
var answers = [];

var transitionSpeed = 400; // ms

function showResults() {
    $(".bar").show();
    $(".fill").animate({
      width: '100%',
    }, 500, function () {});

    $(".bar").each(function(i) {
      $(this).animate({
        width: "" + questions[questionNo].result + '%',
        }, 500, function() {
        // Animation complete.
        });});
    $(step2).show();
    $(".result").fadeIn("slow");
    $(step1).removeClass('highlight');
    $(skip).hide();
}

$(yes).on('click', function( event ) {
    showResults();
    $(no).hide(transitionSpeed);
    $(no).prop("disabled",true);
    answers.push("yes");
    event.preventDefault()
});


$(no).on('click', function( event ) {
    showResults();
    $(yes).hide(transitionSpeed);
    $(yes).prop("disabled",true);
    answers.push("no");
    event.preventDefault()
});


$(start).on('click', function( event ) {
    $(home).hide(transitionSpeed);
    $(instructions).show();
    event.preventDefault()
});

$(begin).on('click', function( event ) {
    $(instructions).hide(transitionSpeed);
    $(step2).hide();
    $(rbox).show();
    showQuestion();
    event.preventDefault()
});

$(next).on('click', function( event ) {
    $(step2).hide();
    questionNo++;
    showQuestion();
    event.preventDefault()
});

$(skip).on('click', function( event ) {
    $(step2).hide();
    questionNo++;
    showQuestion();
    event.preventDefault()
});


var questions = [
    {
        "text": "Did your parents read to you as a child?",
        "result" : 20
    },
    {
        "text": "Can you move around all day without a recurring injury flaring up?",
        "result" : 14
    },
    {
        "text": "Are you comfortable holding hands with your significant other(s) in public?",
        "result" : 23
    },
    {
        "text": "Can you find clothes in your size at a generic clothing store?",
        "result" : 14
    },
    {
        "text": "Do you think of the police as someone you can call for help?",
        "result" : 23
    },
    {
        "text": "Have you studied the history and culture of your ethnic ancestors in primary and/or secondary school?",
        "result" : 44
    },
    {
        "text": "Have you been offered a job with the help of a friend or a family member?",
        "result" : 47
    },
    {
        "text": "Can you walk home at night without fear of being in danger?",
        "result" : 45
    },
    {
        "text": "Can you see a doctor when you need to?",
        "result" : 13
    },
    {
        "text": "Do you commonly relate to people positively portrayed in the media and with whom you share significant aspects of your identity (e.g. race, ethnicity, gender, sexual orientation, ability)?",
        "result" : 44
    },
    {
        "text": "Are you able to attend events without wondering if the main entrance is accessible to you?",
        "result" : 14
    },
    {
        "text": "Have professionals of your race, ethnicity, gender, sexual orientation, *and* ability been positively discussed or publicized within the last month?",
        "result" : 35
    },
    {
        "text": "Is there a national holiday in the country that you live in that honours an aspect/event of your religious/cultural background? (If this doesn't apply to you, skip this question)",
        "result" : 47
    },
    {
        "text": "Have you always felt like your identity was well-described by categorical boxes on a medical form?",
        "result" : 35
    },
    {
        "text": "Can you fall asleep easily once you've decided to fall asleep?",
        "result" : 47
    },
    {
        "text": "Do people always believe you when you say where you're from?",
        "result" : 28
    },
    {
        "text": "Is the gender on your official documents correct?",
        "result" : 6
    },
    {
        "text": "Have you always been able to afford at least 2 meals a day?",
        "result" : 13
    },
    {
        "text": "Can you discuss all aspects of your identity with your family?",
        "result" : 48
    },
    {
        "text": "Do you know someone who could loan you money in a pinch?",
        "result" : 16
    },
    {
        "text": "Are you able to attend events without wondering if there's a bathroom you can use?",
        "result" : 11
    },
];


function showQuestion() {
    if(questionNo == 20) {
        $(rbox).hide();
        $(qbox).hide();
        $(final).show();
        animateBars();
    }else{
        $(yes).show();
        $(no).show();
        $(skip).show();
        $(step1).addClass('highlight');
        $(no).prop("disabled",false);
        $(yes).prop("disabled",false);
        $(qno).text("Question " + (questionNo+1) + "/21");
        $(qtext).text(questions[questionNo].text);
        $(results).text("" + questions[questionNo].result + "% of total responses were no");
        $(qbox).show();
    }
}
