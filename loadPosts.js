document.addEventListener("DOMContentLoaded", function () {
    fetch("posts.json") // Fetch the JSON file
        .then(response => response.json())
        .then(posts => {
            let container = document.getElementById("blog-snippets");
            container.innerHTML = ""; // Clear existing content

            posts.forEach(post => {
                let postHTML = `
                    <article class="blog-snippet">
                        <h3><a href="${post.link}">${post.title}</a></h3>
                        <p><em>${post.date}</em></p>
                        <p>${post.snippet} <a href="${post.link}" class="read-more">Read More</a></p>
                    </article>
                `;
                container.innerHTML += postHTML;
            });
        })
        .catch(error => console.error("Error loading posts:", error));
});
