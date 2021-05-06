package application;
	

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main4 extends Application {
@Override
public void start(Stage primaryStage) {
	try {
		AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main4.fxml"));
		Scene scene = new Scene(root,400,400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		
		TextField tf1 = (TextField) scene.lookup("#tf1");
		TextField tf2 = (TextField) scene.lookup("#tf2");
		TextField tf3 = (TextField) scene.lookup("#tf3");
		Button btn = (Button) scene.lookup("#btn");
		
		btn.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				int tf1_Integer = Integer.parseInt(tf1.getText());
				int tf2_Integer = Integer.parseInt(tf2.getText());
				int result = 0;
				
				for(int i = tf1_Integer ; i <= tf2_Integer ; i++) {
					result += i;
				}
				
				tf3.setText(result + "");
			}
		
		});
		
		primaryStage.setScene(scene);
		primaryStage.show();
	} catch(Exception e) {
		e.printStackTrace();
	}
}

public static void main(String[] args) {
	launch(args);
}
}