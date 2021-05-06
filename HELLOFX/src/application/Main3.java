package application;
	


import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main3 extends Application {
@Override
public void start(Stage primaryStage) {
	try {
		AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main3.fxml"));
		Scene scene = new Scene(root,400,400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		
		TextField tf1 = (TextField) scene.lookup("#tf1");
		TextField tf2 = (TextField) scene.lookup("#tf2");
		TextField tf3 = (TextField) scene.lookup("#tf3");
		Button btn1 = (Button) scene.lookup("#btn1");
		Button btn2 = (Button) scene.lookup("#btn2");
		Button btn3 = (Button) scene.lookup("#btn3");
		Button btn4 = (Button) scene.lookup("#btn4");
		
		btn1.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				int tf1_Integer = Integer.parseInt(tf1.getText());
				int tf2_Integer = Integer.parseInt(tf2.getText());
				
				int result = tf1_Integer + tf2_Integer;
				tf3.setText(result+"");
			}
		});
		btn2.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				int tf1_Integer = Integer.parseInt(tf1.getText());
				int tf2_Integer = Integer.parseInt(tf2.getText());
				
				int result = tf1_Integer - tf2_Integer;
				tf3.setText(result+"");
			}
		});
		btn3.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				int tf1_Integer = Integer.parseInt(tf1.getText());
				int tf2_Integer = Integer.parseInt(tf2.getText());
				
				int result = tf1_Integer * tf2_Integer;
				tf3.setText(result+"");
			}
		});
		btn4.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				int tf1_Integer = Integer.parseInt(tf1.getText());
				int tf2_Integer = Integer.parseInt(tf2.getText());
				
				int result = tf1_Integer / tf2_Integer;
				tf3.setText(result+"");
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