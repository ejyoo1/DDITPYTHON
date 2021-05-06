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


public class Main5 extends Application {
@Override
public void start(Stage primaryStage) {
	try {
		AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main5.fxml"));
		Scene scene = new Scene(root,400,400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		
		TextField tfMine = (TextField) scene.lookup("#tfMine");
		TextField tfCom = (TextField) scene.lookup("#tfCom");
		TextField tfResult = (TextField) scene.lookup("#tfResult");
		Button btn = (Button) scene.lookup("#btn");
		
		
		btn.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String tfMineString = tfMine.getText();
				String tfComString = tfCom.getText();
				String result = "";

				double rnd = Math.random();
				if(rnd > 0.5) {
					tfComString = "홀";
				} else {
					tfComString = "짝";
				}
				
				if(tfMineString.equals(tfComString)){
					result = "성공";
				} else {
					result = "실패";
				}
				
				tfCom.setText(tfComString);
				tfResult.setText(result);
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