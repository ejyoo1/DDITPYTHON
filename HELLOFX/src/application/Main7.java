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


public class Main7 extends Application {
@Override
public void start(Stage primaryStage) {
	try {
		AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main7.fxml"));
		Scene scene = new Scene(root,400,400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		
		TextField tfMine = (TextField) scene.lookup("#tfMine");
		TextField tfCom = (TextField) scene.lookup("#tfCom");
		TextField tfResult = (TextField) scene.lookup("#tfResult");
		Button btn = (Button) scene.lookup("#btn");
		
		btn.setOnMouseClicked(new EventHandler<Event>() {
			@Override
			public void handle(Event event) {
				String mine = tfMine.getText();
				String com = "";
				String result = "";
				double rnd = Math.random();

				if(rnd > 0.66) {
					com = "가위";
				}else if(rnd > 0.33) {
					com = "바위";
				}else {
					com = "보";
				}
				
				if("가위".equals(mine) && "가위".equals(com)) {
					result = "비김";
				}
				if("가위".equals(mine) && "바위".equals(com)) {
					result = "짐";
				}
				if("가위".equals(mine) && "보".equals(com)) {
					result = "이김";
				}
				
				if("바위".equals(mine) && "바위".equals(com)) {
					result = "비김";
				}
				if("바위".equals(mine) && "보".equals(com)) {
					result = "짐";
				}
				if("바위".equals(mine) && "가위".equals(com)) {
					result = "이김";
				}
				
				if("보".equals(mine) && "보".equals(com)) {
					result = "비김";
				}
				if("보".equals(mine) && "가위".equals(com)) {
					result = "짐";
				}
				if("보".equals(mine) && "바위".equals(com)) {
					result = "이김";
				}
				
				tfCom.setText(com);
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