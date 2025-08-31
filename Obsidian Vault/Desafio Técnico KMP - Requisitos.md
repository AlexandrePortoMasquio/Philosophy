### Mobile App - Take Home Assignment

You should supply the code for review, be ready to reference it for the follow-up technical interview, and be ready to present the code via Screen Share.

The purpose of this assignment is to provide us with a sample of how you structure your software and what architectural approach you will implement. It should be representative of what you would do on a professional level. It should be representative of what you would do as a professional during your day to day on the job. Please take the time to review the grading criteria below.

#### How will it be graded?
- Solution works.
- Code is clean, well-written, easy to read and contains documentation.
- Functionally works and satisfies the requirements below.
- Thoughtful design and user experience is a plus.
- Code is unit tested. Other kinds of tests will be considered pluses.

We incentivize you to perform mindful choices in your software solution and document them in a README, so the evaluators can follow your train of thought. If you cannot meet all the requirements (due to time constraints or any other reasons), be sure to implement that as well. If you provide a list of things you would pick to implement next if you were to maintain this project for a long-time, that will be taken as a plus.

#### Take Home Assignment – Local Sake Shops (Native Apps Android and iOS)

For this assignment, you will build a simple app that allows the user to see 1) a screen with a list of local sake shops and 2) a details screen for a specific sake shop.

#### Requirements
The data is going to be supplied in JSON format.

The list page should contain items with sake shop names, address, and star ratings. Whenever a sake shop from the list is tapped, the user should be directed to the details page of that shop.

The details page should contain details about the sake shops, including:
- Shop name.
- Shop picture.
- A brief description.
- A rating in stars.
- Address (clickable, should open address in a Maps app or browser).
- A button or link to visit the shop's website in default web browser or in a custom tab.

#### Instructions
1. Build at least one component that displays all items from the supplied JSON data you got together with this assignment.

2. You will be evaluated based on at least some of the following:
   a. Software architecture and solution design.
   b. Re-usability of your solution (could someone re-implement your solution easily for a different type of data / different API? Could a Web version be built reusing your entities and use cases?).
   c. Good UX and UI will be considered pluses, but you don't need to spend a very long time pixel-perfecting the look and feel (we don't expect you to be a designer). Follow material design guidelines and you're good.
   d. Other factors include: any tests included, component structure and standards, performance and stability, etc.

3. You can either use Kotlin and Swift UI.

4. (Plus) You can use hybrid tools like Kotlin multiplatform for the business and data layers. If you want to do so, clone this project and use it as base.

Note: UIKit submissions will not be accepted.

#### Submission
Your app should be able to run in simulators. Please zip the project folder (run ./gradlew clean before zipping) and be sure to include in your README how to set up dependencies if your solution requires it. It would be great if you could also include an APK file if it's an Android app.

---

Ver também: [[Explicação do Desafio KMP]]
