### Cloud Rest service with Servlet

```java
public class VideoServlet extends HttpServlet{

	/* 
	query the list of videos sent to server, we are only storing in memory, if server is shutdown servlet is not
	going to remember what videos have been uploaded. 
	video object tracks information like name, url, duration
	*/
	private List<Video> videos = new ArrayList<Video>;
	
	
	/*
	If someone sends a GET request doGet method on our servlet will be invoked
	*/
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
		
		// servlet wants to tell the client how to interpret the result its sending back, mimetype is set to text
		resp.setContentType("text/plain");
		
		// Loop through all the stored videos ands print them out for the client to see 
		PrintWriter sendToClient = resp.GetWriter();
		for(Video v:this.video){
			sendToClient.write(v.getName() + ":" + v.getUrl() + "\n");
		}
	
	}
	
	
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{

	/*
		we want the client to be able to send us information about a video 
		the client is going to in encode that information either as query parameters or as a body of an HTTP post in this case.
		We have to extract that data 
	*/
	
	//extract the video properties
	String name = req.getParameter("name");
	String url = req.getParameter("url");
	String durationStr = req.getParameter("duration");
	
	// set the response content type 
	resp.setContentType("text/plain");
	
	
	// Error checking to make sure Client sent us valid and correct values 
	if (
		name == null || 
		url == null  || 
		durationStr == null || 
		name.trim().length() < 1 ||
		url.trim().length() < 10 ||
		durationStr.trim().length() < 1 ||)
		{
			// Error Code and message 
			resp.sendError(400);
			resp.getWriter.write("Missing ['name', 'duration', 'url']);
		}
	else {
		// parsing and convert String to Java native types 
		long duration = Long.parseLong(durationStr);
		Video v = new Video(name, url, duration);
		videos.add(v)
		resp.getWriter().write("Video added ");
	}
	
	
	
	}
}
```


### Request Routing and Web.xml


How does the web application container that our servlet is running in know when should it invoke our servlet and which operations it should handle? we need a routing relationship this is stored in web.xml. Newer apps use Java-based configurations.

```xml
<web-app xmlns="https://java.sun.com/xmls/ns/j2ee" version="2.4" xmlns:xsi="http://" xmlns:schemaLocation="http://">
	
	<!-- defining/declaring -->
	<servlet>
		<servlet-name>video</servlet-name>
		<servlet-class>org.mobilecloud.VideoServlet</servlet-class>
	</servlet>
	<!-- routing -->
	<servlet-mapping>
		<servlet-name>video</servlet-name>
		<url-pattern>/video</url-pattern>
	</servlet-mapping>
</webapp>
```

