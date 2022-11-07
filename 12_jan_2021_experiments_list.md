iiwa7.move(ptp(1.3532,1.0490,-0.7183,1.8372,0.5674,2.0256,-0.5882));
		Frame P1 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(1.3720,1.2748,-1.0698,2.0102,0.3806,1.9460,-0.3189));
		Frame P2 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.4028,1.9868,-1.9607,1.4210,-2.7489,0.5597,2.2765));
		Frame P3 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-1.4908,1.2321,-1.2708,1.3960,-2.8445,1.5627,-2.8029));
		Frame P4 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.2420,1.9327,-1.8786,1.3499,-2.6784,0.4976,2.3060));
		Frame P5 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.7170,2.0050,-2.1780,1.7768,-2.6954,0.4901,2.0362));
		Frame P6 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-1.6521,1.2104,-1.2399,1.4229,-2.7727,1.6714,-2.7793));
		Frame P7 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.6507,1.0243,-0.8552,1.6463,2.5830,0.5665,-1.8231));
		Frame P8 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());
		iiwa7.move(ptp(-0.1385,1.2957,-1.2986,1.5222,2.2333,0.2962,-1.9458));
		Frame P9 = iiwa7.getCurrentCartesianPosition(iiwa7.getFlange());



double override = 1;
		getApplicationControl().setApplicationOverride(override);
		
		DataRecorder rec1=new DataRecorder("LogFile_1.log",600,TimeUnit.SECONDS,20);


rec1.addCommandedJointPosition(iiwa7, AngleUnit.Degree);
		rec1.addCurrentJointPosition(iiwa7, AngleUnit.Degree);


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