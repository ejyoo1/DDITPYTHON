package application;
	

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main2 extends Application {
@Override
public void start(Stage primaryStage) {
	try {
		AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main2.fxml"));
		Scene scene = new Scene(root,400,400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		
		Label lbl = (Label) scene.lookup("#lbl");
		Button btn = (Button) scene.lookup("#btn");
		
		btn.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String lblString = lbl.getText();
				int lblNumber = Integer.parseInt(lblString);
				lblNumber++;
				lbl.setText(lblNumber+"");
//				lbl.setText(Integer.toString(number));
			}
		});
		
		Label lbl_decrease = (Label) scene.lookup("#lbl_decrease");
		Button btn_decrease = (Button) scene.lookup("#btn_decrease");
		
		btn_decrease.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				int number = Integer.parseInt(lbl_decrease.getText()) - 1;
				lbl_decrease.setText(Integer.toString(number));
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