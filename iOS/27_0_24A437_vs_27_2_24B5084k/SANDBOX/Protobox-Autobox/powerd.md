## powerd

> Group: ⬆️ Updated

```diff

 	)
 )
 
-(deny iokit-set-properties)
+(deny iokit-set-properties
+	(require-all
+		(iokit-property "ExternalConnected")
+		(require-not (iokit-registry-entry-class "AppleSmartBattery"))
+		(require-not (iokit-registry-entry-class "AppleARMPMUCharger"))
+	)
+)
+(deny iokit-set-properties
+	(require-all
+		(iokit-property "ShipChargeLimitData")
+		(require-not (iokit-registry-entry-class "AppleSmartBattery"))
+	)
+)
+(deny iokit-set-properties
+	(require-all
+		(iokit-property "CarrierModeStatus")
+		(require-not (iokit-registry-entry-class "AppleSmartBattery"))
+		(require-not (iokit-registry-entry-class "AppleARMPMUCharger"))
+	)
+)
+(deny iokit-set-properties
+	(require-all
+		(require-any
+			(iokit-property "CriticalAcOverride")
+			(iokit-property "DateOfFirstUse")
+		)
+		(require-not (iokit-registry-entry-class "AppleSmartBattery"))
+	)
+)
+(deny iokit-set-properties
+	(require-all
+		(require-any
+			(iokit-property "CarrierModeHighVoltage")
+			(iokit-property "CarrierModeLowVoltage")
+		)
+		(require-not (iokit-registry-entry-class "AppleSmartBattery"))
+	)
+)
+(deny iokit-set-properties
+	(require-any
+		(require-not (iokit-registry-entry-class "AppleBTM"))
+		(require-not (require-any
+			(iokit-property "AlgoTemperature")
+			(iokit-property "CaptureTime")
+			(iokit-property "ChargeAccum")
+			(iokit-property "DataCaptureTrigger")
+			(iokit-property "InstantAmperage")
+			(iokit-property "PresentDOD")
+			(iokit-property "VirtualTemperature")
+		))
+	)
+)
 
 (deny ipc*)
 
```
