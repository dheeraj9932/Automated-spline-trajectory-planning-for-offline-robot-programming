package application;


import java.util.Vector;
import java.util.concurrent.TimeUnit;

import javax.inject.Inject;
import com.kuka.roboticsAPI.applicationModel.RoboticsAPIApplication;
import static com.kuka.roboticsAPI.motionModel.BasicMotions.*;

import com.kuka.roboticsAPI.deviceModel.JointPosition;
import com.kuka.roboticsAPI.deviceModel.LBR;
import com.kuka.roboticsAPI.geometricModel.Frame;
import com.kuka.roboticsAPI.motionModel.MotionBatch;
import com.kuka.roboticsAPI.motionModel.Spline;
import com.kuka.roboticsAPI.motionModel.SplineJP;
import com.kuka.roboticsAPI.motionModel.SplineMotionJP;
import com.kuka.roboticsAPI.motionModel.SplineOrientationType;
import com.kuka.roboticsAPI.sensorModel.DataRecorder;
import com.kuka.roboticsAPI.sensorModel.DataRecorder.AngleUnit;
import com.kuka.roboticsAPI.uiModel.ApplicationDialogType;

/**
 * Implementation of a robot application.
 * <p>
 * The application provides a {@link RoboticsAPITask#initialize()} and a 
 * {@link RoboticsAPITask#run()} method, which will be called successively in 
 * the application lifecycle. The application will terminate automatically after 
 * the {@link RoboticsAPITask#run()} method has finished or after stopping the 
 * task. The {@link RoboticsAPITask#dispose()} method will be called, even if an 
 * exception is thrown during initialization or run. 
 * <p>
 * <b>It is imperative to call <code>super.dispose()</code> when overriding the 
 * {@link RoboticsAPITask#dispose()} method.</b> 
 * 
 * @see UseRoboticsAPIContext
 * @see #initialize()
 * @see #run()
 * @see #dispose()
 */
public class Bewegungs_test extends RoboticsAPIApplication {
	@Inject
	private LBR iiwa7;
	
	@Override
	public void initialize() {
		// initialize your application here
	}
	
    @Override
    public void dispose() {
    }

	@Override
	public void run() {
		// your application execution starts here
		
		iiwa7.move(ptp(1.3532,1.049,-0.7183,1.8372,0.5674,2.0256,-0.5882));
		Frame P1 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(1.372,1.2748,-1.0698,2.0102,0.3806,1.946,-0.3189));
		Frame P2 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.4028,1.9868,-1.9607,1.421,-2.7489,0.5597,2.2765));
		Frame P3 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-1.4908,1.2321,-1.2708,1.396,-2.8445,1.5627,-2.8029));
		Frame P4 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.242,1.9327,-1.8786,1.3499,-2.6784,0.4976,2.306));
		Frame P5 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.717,2.005,-2.178,1.7768,-2.6954,0.4901,2.0362));
		Frame P6 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-1.6521,1.2104,-1.2399,1.4229,-2.7727,1.6714,-2.7793));
		Frame P7 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.6507,1.0243,-0.8552,1.6463,2.583,0.5665,-1.8231));
		Frame P8 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.1385,1.2957,-1.2986,1.5222,2.2333,0.2962,-1.9458));
		Frame P9 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.2221,1.1204,-1.1176,1.4716,2.2729,0.4628,-1.7945));
		Frame P10 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.3342,1.9507,-2.1244,1.8426,-1.7236,0.4092,1.2));
		Frame P11 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(1.2902,1.1661,-0.8842,1.9531,0.5241,1.932,-0.4344));
		Frame P12 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-1.3773,1.1884,-1.2995,1.1755,-2.8343,1.66,-2.7576));
		Frame P13 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-1.4983,1.097,-1.2383,1.1339,-2.7157,1.7507,-2.6594));
		Frame P14 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.1637,1.2536,-1.1564,1.7735,1.4734,0.3601,-1.0868));
		Frame P15 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.1111,1.0732,-1.1993,1.1782,2.5379,0.5807,-2.0863));
		Frame P16 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.5434,1.9147,-2.1757,2.0176,-1.8325,0.3634,1.2484));
		Frame P17 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		//iiwa7.move(ptp(-0.1217,1.0310,-1.1466,1.2040,2.4570,0.5898,-1.9631));
		//Frame P11 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		
		
		

		
		//Frame P1 =getApplicationData().getFrame("/P1").copyWithRedundancy();
		//Frame P2 =getApplicationData().getFrame("/P2").copyWithRedundancy();
		//Frame P3 =getApplicationData().getFrame("/P3").copyWithRedundancy();
		//Frame P4 =getApplicationData().getFrame("/P4").copyWithRedundancy();
		//Frame P5 =getApplicationData().getFrame("/P5").copyWithRedundancy();
		//Frame P6 =getApplicationData().getFrame("/P6").copyWithRedundancy();
	    //Frame P7 =getApplicationData().getFrame("/P7").copyWithRedundancy();
		////Frame P8 =getApplicationData().getFrame("/P8").copyWithRedundancy();
		//Frame P9 =getApplicationData().getFrame("/P9").copyWithRedundancy();
		//Frame P10=getApplicationData().getFrame("/P10").copyWithRedundancy();
		//Frame P11 =getApplicationData().getFrame("/P11").copyWithRedundancy();
	   // Frame P12 =getApplicationData().getFrame("/P12").copyWithRedundancy();
		//Frame P13 =getApplicationData().getFrame("/P13").copyWithRedundancy();
		//Frame P14 =getApplicationData().getFrame("/P14").copyWithRedundancy();
		//Frame P15=getApplicationData().getFrame("/P15").copyWithRedundancy();
		double override = 1;
		getApplicationControl().setApplicationOverride(override);
		
		DataRecorder rec1=new DataRecorder("LogFile_1.log",600,TimeUnit.SECONDS,20);
//		rec1.setFileName("LogFile_1.log");
//		rec1.setTimeout(200,TimeUnit.SECONDS);
//		rec1.setSampleRate(TimeUnit.SECONDS,20);
		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
		//rec1.addCommandedCartesianPositionXYZ(measureFrame, referenceFrame);
		
//		DataRecorder rec2=new DataRecorder();
//		rec1.setFileName("LogFile_2.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
//		
//		DataRecorder rec3=new DataRecorder();
//		rec1.setFileName("LogFile_3.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
//		
//		DataRecorder rec4=new DataRecorder();
//		rec1.setFileName("LogFile_4.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
//		
//		DataRecorder rec5=new DataRecorder();
//		rec1.setFileName("LogFile_5.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
//		
//		DataRecorder rec6=new DataRecorder();
//		rec1.setFileName("LogFile_6.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
//		
//		DataRecorder rec7=new DataRecorder();
//		rec1.setFileName("LogFile_7.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
//		
//		
//		DataRecorder rec8=new DataRecorder();
//		rec1.setFileName("LogFile_8.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
//		
//		DataRecorder rec9=new DataRecorder();
//		rec1.setFileName("LogFile_9.log");
//		//rec1.setTimeout(600,TimeUnit.SECONDS);
//		rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
//		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);
		
		
		
		
		rec1.enable();
		rec1.startRecording();
		iiwa7.move(ptpHome());	
		iiwa7.move(ptp(P1));
		Spline test1 = new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test1);
		iiwa7.move(ptpHome());
		
		
		
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test2=new Spline(spl(P2),spl(P3),circ(P4,P5),spl(P6),spl(P7));
		iiwa7.move(test2);
		iiwa7.move(ptpHome());
		
		
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test31=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P1));
		iiwa7.move(test31);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test32=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P2));
		iiwa7.move(test32);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test33=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P3));
		iiwa7.move(test33);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test34=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P4));
		iiwa7.move(test34);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test35=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P6));
		iiwa7.move(test35);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test36=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P7));
		iiwa7.move(test36);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test37=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P8));
		iiwa7.move(test37);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test38=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P9));
		iiwa7.move(test38);
		iiwa7.move(ptpHome());
		
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test41=new Spline(spl(P2),spl(P3),spl(P1),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test41);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test42=new Spline(spl(P2),spl(P3),spl(P2),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test42);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test43=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test43);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test44=new Spline(spl(P2),spl(P3),spl(P5),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test44);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test45=new Spline(spl(P2),spl(P3),spl(P6),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test45);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test46=new Spline(spl(P2),spl(P3),spl(P7),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test46);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test47=new Spline(spl(P2),spl(P3),spl(P8),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test47);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test48=new Spline(spl(P2),spl(P3),spl(P8),spl(P5),spl(P6),spl(P7));
		iiwa7.move(test48);
		iiwa7.move(ptpHome());
		
		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test51=new Spline(spl(P3),spl(P4));
		iiwa7.move(test51);
		iiwa7.move(ptpHome());
		

		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test52=new Spline(spl(P2),spl(P3));
		iiwa7.move(test52);
		iiwa7.move(ptpHome());
		

		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P1));
		Spline test53=new Spline(spl(P2));
		iiwa7.move(test53);
		iiwa7.move(ptpHome());
		

		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P2));
		Spline test54=new Spline(spl(P3));
		iiwa7.move(test54);
		iiwa7.move(ptpHome());
		

		iiwa7.move(ptpHome());
		iiwa7.move(ptp(P3));
		Spline test55=new Spline(spl(P4));
		iiwa7.move(test55);
		iiwa7.move(ptpHome());
		
		
		
	
		
		
		//MotionBatch mb = new MotionBatch(ptp(P1),circ(P2,P3),ptp(P4),lin(P5));
		//Spline CS = new Spline(spl(P2),spl(P3),spl(P4));
		//SplineJP JS = new SplineJP(ptp(Math.toRadians(27.04),Math.toRadians(8.66), Math.toRadians(21.88), Math.toRadians(-109.21), 0, Math.toRadians(32.51), Math.toRadians(90)),ptp(Math.toRadians(9.39),Math.toRadians(5.68), Math.toRadians(8.72), Math.toRadians(-101.94), 0, Math.toRadians(32.51), Math.toRadians(90)),ptp(Math.toRadians(-53.15), Math.toRadians(1.6), Math.toRadians(8.72), Math.toRadians(-100.51), 0, Math.toRadians(32.51), Math.toRadians(90)), ptp(Math.toRadians(-53.15),Math.toRadians(1.6), Math.toRadians(8.73), Math.toRadians(-69.27), Math.toRadians(-13.83), Math.toRadians(33.06), Math.toRadians(90)));
		//Spline SP1= new Spline(spl(P1));
		
//		iiwa7.move(ptp(P1));
//		Spline testp2p6=new Spline(spl(P2),spl(P3),spl(P4),spl(P5).setOrientationType(SplineOrientationType.Ignore),spl(P6));
//		iiwa7.move(testp2p6);
		
		
		//iiwa7.move(ptp(P1));
		//Spline test61=new Spline(spl(P2),spl(P3).setOrientationType(SplineOrientationType.Ignore),lin(P8).setOrientationType(SplineOrientationType.Ignore),spl(P5).setOrientationType(SplineOrientationType.Ignore),lin(P9).setOrientationType(SplineOrientationType.Ignore),spl(P7));
		//iiwa7.move(test61);
		//iiwa7.move(ptpHome());
		//iiwa7.move(ptp(P1));
		//Spline test52=new Spline(spl(P2),spl(P3).setOrientationType(SplineOrientationType.Ignore),spl(P4).setOrientationType(SplineOrientationType.Ignore),circ(P5,P9).setOrientationType(SplineOrientationType.Ignore),spl(P7));
		//iiwa7.move(test52);
		//iiwa7.move(ptpHome());
		//iiwa7.move(ptp(P1));
		//Spline test62=new Spline(spl(P2),spl(P3).setOrientationType(SplineOrientationType.Ignore),spl(P8).setOrientationType(SplineOrientationType.Ignore),circ(P5,P9).setOrientationType(SplineOrientationType.Ignore),spl(P7));
		//iiwa7.move(test62);
		//iiwa7.move(ptpHome());
		
		//Spline test41=new Spline(spl(P2),	spl(P3), spl(P8),spl(P5),lin(P6),spl(P7));
		//iiwa7.move(test41);
		//iiwa7.move(ptpHome());
		//iiwa7.move(ptp(P1));
		//Spline test2=new Spline(spl(P2),spl(P3),spl(P4),spl(P5).setOrientationType(SplineOrientationType.Ignore),lin(P6).setOrientationType(SplineOrientationType.Ignore),spl(P7));
		
		
		
//		iiwa7.move(ptpHome());
//		iiwa7.move(ptp(P1));
	//	Spline test51=new Spline(spl(P2),spl(P3),spl(P4),spl(P5),lin(P9),spl(P7));
	//    iiwa7.move(test51);
//		iiwa7.move(ptpHome());
	//	iiwa7.move(ptp(P1));
		
		
		
		//Spline test6=new Spline(spl(P2),spl(P3),spl(P8),spl(P5),spl(P7),spl(P9));
				//iiwa7.move(test6);
				//iiwa7.move(ptpHome());
				//iiwa7.move(ptp(P1));
				
		
		//iiwa7.move(SP1);
		//iiwa7.move(ptp(P1));
		//iiwa7.move(SP2);
				

	}
	
}