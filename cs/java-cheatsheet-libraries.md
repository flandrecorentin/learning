
# java.net.http, com.fasterxml.jackson.(databind)

````java
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.NoArgsConstructor;

@Builder
@NoArgsConstructor
@AllArgsConstructor
@lombok.Data
public class Data {
    // @JsonProperty("json_name")
    // @JsonFormat(shape = JsonFormat.Shape.STRING, timezone = "UTC+2:00", pattern = "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'")

    private int id;
    private String job;
}

// -----------------------------------------------------
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.text.SimpleDateFormat;
import java.util.Collections;
import java.util.List;

public class Client {

    public static final Logger LOGGER = LogManager.getLogger(Client.class);
    public static final String URL_ENDPOINT = "";
    private static final ObjectMapper mapper = new ObjectMapper().configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
            .registerModule(new JavaTimeModule()).setDateFormat(new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"));

    public List<Data> getInformation() {
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder().uri(URI.create(URL_ENDPOINT))
                    .header("Content-Type", "application/json")
                    .header("Authorization", "Bearer " + "sampleApiKey")
//                    .header("Authorization", authorization)
                    .build();

            LOGGER.debug("request created");
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            LOGGER.debug(response.statusCode());
            List<Data> infos = mapper.readValue(response.body(), new TypeReference<>() {
            });

            LOGGER.debug("Infos retrieve: {}", infos);
            return infos;
        } catch (Exception ex) {
            ex.printStackTrace();
            return Collections.emptyList();
        }
    }

    public int postInformation(List<Data> infos) {
        try {
            // LOGGER.debug("Serialized result to post: {}", mapper.writeValueAsString(infos));
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder().uri(URI.create(URL_ENDPOINT))
                    .header("Content-Type", "application/json")
                    .header("Authorization", "Bearer " + "sampleApiKey")
                    .POST(HttpRequest.BodyPublishers.ofString(mapper.writeValueAsString(infos))).build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            LOGGER.debug("Response status code: {}", response.statusCode());
            LOGGER.debug("Response body: {}", response.body());

            return response.statusCode();
        } catch (Exception ex) {
            ex.printStackTrace();
            return -1;
        }
    }
}

// ---------------------------------------------

<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.hubspot</groupId>
    <artifactId>coding-assessment</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <version.log4j.api>2.23.1</version.log4j.api>
        <version.log4j.core>2.23.1</version.log4j.core>
        <version.jackson>2.17.2</version.jackson>
        <version.lombok>1.18.30</version.lombok>
        <version.lombok.datatype>2.15.2</version.lombok.datatype>
        <version.junit>5.8.2</version.junit>
        <version.junit.mockito>5.12.0</version.junit.mockito>
        <version.mockito>4.2.0</version.mockito>
    </properties>

    <dependencies>
        <!--        LOGGER      -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
            <version>${version.log4j.api}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>${version.log4j.core}</version>
        </dependency>

        <!--        UTILS      -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>${version.jackson}</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.datatype</groupId>
            <artifactId>jackson-datatype-jsr310</artifactId>
            <version>${version.lombok.datatype}</version>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>${version.lombok}</version>
            <scope>provided</scope>
        </dependency>

        <!--        TEST       -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${version.junit}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>${version.mockito}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-junit-jupiter</artifactId>
            <version>${version.junit.mockito}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>


// In src/main/resources
<Configuration status="info">
    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{yyyy-DDD-HH:mm:ss} %-5p %m%n"/>
        </Console>
    </Appenders>
    <Loggers>
        <Root level="debug">
            <AppenderRef ref="Console"/>
        </Root>
    </Loggers>
</Configuration>

````