// script.js
console.log('Script loaded successfully');

function showSection(sectionId) {
    console.log('showSection called with:', sectionId); // Debug log
    
    // Hide all sections
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.style.display = 'none'; // Hide all sections
    });

    // Show the selected section
    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.style.display = 'block'; // Show the selected section
        console.log('Showing section:', sectionId); // Debug log
    } else {
        console.error('Section not found:', sectionId); // Error log
    }
}
