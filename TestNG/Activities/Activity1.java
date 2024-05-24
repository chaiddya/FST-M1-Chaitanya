package Activities;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class Activity1 {

    WebDriver driver;

    @BeforeClass
    public void SetUp() {
        // Set up Firefox driver
        WebDriverManager.firefoxdriver().setup();
        // Create a new instance of the Firefox driver
        driver = new FirefoxDriver();

        // Open the page
        driver.get("https://v1.training-support.net");
    }

    @Test
    public void homepageTest() {
        // Assert page title
        Assert.assertEquals(driver.getTitle(), "Training Support");

        // Find About Us link using id and click it
        driver.findElement(By.id("about-link")).click();
        // Print the title of the new page
        Assert.assertEquals(driver.getTitle(), "About Training Support");
    }

    @AfterClass
    public void teardown() {
        //close the browser
        driver.quit();
    }

}
