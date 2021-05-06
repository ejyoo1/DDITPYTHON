package application;
	

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main9 extends Application {
@Override
public void start(Stage primaryStage) {
	try {
		AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main9.fxml"));
		Scene scene = new Scene(root,400,400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		
		TextField tf = (TextField) scene.lookup("#tf");
		Button btn1 = (Button) scene.lookup("#btn1");
		Button btn2 = (Button) scene.lookup("#btn2");
		Button btn3 = (Button) scene.lookup("#btn3");
		Button btn4 = (Button) scene.lookup("#btn4");
		Button btn5 = (Button) scene.lookup("#btn5");
		Button btn6 = (Button) scene.lookup("#btn6");
		Button btn7 = (Button) scene.lookup("#btn7");
		Button btn8 = (Button) scene.lookup("#btn8");
		Button btn9 = (Button) scene.lookup("#btn9");
		Button btn0 = (Button) scene.lookup("#btn0");
		Button btnCall = (Button) scene.lookup("#btnCall");
		
		btn1.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn1.getText(); 
				tf.setText(result);
			}
		});
		
		btn2.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn2.getText(); 
				tf.setText(result);
			}
		});
		
		btn3.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn3.getText(); 
				tf.setText(result);
			}
		});
		
		btn4.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn4.getText(); 
				tf.setText(result);
			}
		});
		
		btn1.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn1.getText(); 
				tf.setText(result);
			}
		});
		
		btn5.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn5.getText(); 
				tf.setText(result);
			}
		});
		
		btn6.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn6.getText(); 
				tf.setText(result);
			}
		});
		
		btn7.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn7.getText(); 
				tf.setText(result);
			}
		});
		
		btn8.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn8.getText(); 
				tf.setText(result);
			}
		});
		
		btn9.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn9.getText(); 
				tf.setText(result);
			}
		});
		
		btn0.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				result += btn0.getText(); 
				tf.setText(result);
			}
		});
		
		
		
		
		
		
		btnCall.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String result = tf.getText();
				
				Alert alert = new Alert(AlertType.INFORMATION);
				alert.setTitle("Information Dialog");
				alert.setHeaderText("Look, a Information Dialog");
				alert.setContentText(result);

				alert.showAndWait();
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