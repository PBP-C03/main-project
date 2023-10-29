$(document).ready(function() {
    $("#add-question-btn").click(function() {
        $("#add-question-modal").modal('show');
    });

$(document).ready(function() {
    // Function to handle search input
    $("#search-bar").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#question-data tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

    

    const dataElement = document.getElementById('my-data');
    const getQuestionDataUrl = dataElement.dataset.getQuestionDataUrl;
    const askQuestionUrl = dataElement.dataset.askQuestionUrl;
    async function getData(){
        $.ajax({
            url: getQuestionDataUrl,
                type: "GET",
                success: function(response) {
                    // Clear existing data
                    $("#question-data").empty();

                    // Append the new question data to the table
                    for (var i = 0; i < response.questions.length; i++) {
                        var newRow = "<tr><td>" + response.questions[i].user_name + "</td><td>" + response.questions[i].question_title + "</td><td>" + response.questions[i].book_name + "</td><td>" + response.questions[i].question + "</td><td><button class='btn btn-primary add-comment-btn' data-toggle='modal' data-target='#add-comment-modal' data-question='" + response.questions[i].question + "'>Add Comment</button></td><td><button class='btn btn-danger delete-question-btn' data-question-id='" + response.questions[i].id + "'>Delete</button></td></tr>";
                        $("#question-data").append(newRow);
                    }

                    $("#question-table").show()
                },
                error: function(error) {
                    console.error(error);
                }
            });
    }

    $("#question-form").submit(function(event) {
        event.preventDefault();

        var title = $('#title').val()
        var content = $('#content').val()
        var book = document.getElementById("book").value;

        $.ajax({
            url: askQuestionUrl,
            type: "POST",
            headers: {'X-CSRFToken': '{{ csrf_token }}'},  // Add this line
            data: {
                title: title,
                content: content,
                book: parseInt(book),
            },
            success: function(response) {
                console.log(response);
                if(response.result == 'Success!') {
                    $("#add-question-modal").modal('hide');
                    // This is where you retrieve the data after submission
                    getData();
                    $("#question-table").show();  // Menampilkan tabel setelah mendapatkan data baru
                } else {
                    // Handle form validation error here
                    console.log(response.errors);
                }
            },
            error: function(error) {
                // Handle request error here
                console.error(error);
            }
        });
    });
getData()



$(document).on('click', '.delete-question-btn', function() {
var questionId = $(this).data('question-id');
var userId = $(this).data('user-id');
var url = $(this).data('url');
var currentUserId = "{{ request.user.id }}";  // Tambahkan baris ini

// Tambahkan pengecekan ini
if (currentUserId != userId) {
    alert("You are not the creator of this question.");
    return;
}

$.ajax({
    url: url, // Use the URL from the data attribute
    type: "POST",
    headers: {'X-CSRFToken': '{{ csrf_token }}'},
    success: function(response) {
        console.log(response);
        if(response.result == 'Success!') {
            getData(); // Refresh the data after deletion
        } else {
            console.log(response.errors);
            // Display the error message to the user
            alert(response.errors);
        }
    },
    error: function(error) {
        console.error(error);
    }
});
});

$(document).on('click', '.add-comment-btn', function() {
    var questionId = $(this).data('question-id');
    $('#comment-form').data('question-id', questionId);  // Store the question id in the comment form
    $('#add-comment-modal').modal('show');
});

$('#comment-form').submit(function(event) {
    event.preventDefault();

    var questionId = $(this).data('question-id'); // Retrieve the stored question id
    var content = $('#content').val();

    $.ajax({
        url: "/qna/add_comment/" + questionId + "/",
        type: "POST",
        headers: {'X-CSRFToken': '{{ csrf_token }}'},
        data: {
            content: content,
        },
        success: function(response) {
            console.log(response);
            if(response.result == 'Success!') {
                // Refresh the page or show a success message to the user
                getData();  // Assuming you have a function to refresh the data
            } else {
                // Handle form validation error here
                console.log(response.errors);
            }
        },
        error: function(error) {
            // Handle request error here
            console.error(error);
        }
    });
});


});

