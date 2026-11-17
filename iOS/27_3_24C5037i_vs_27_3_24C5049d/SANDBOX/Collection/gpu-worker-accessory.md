## gpu-worker-accessory

> Group: ⬆️ Updated

```diff

 
 (allow iokit-get-properties
 	(require-all
+		(iokit-registry-entry-class "IOAcceleratorES")
 		(require-any
 			(iokit-property "MetalPluginClassName")
 			(iokit-property "MetalPluginName")
 		)
-		(iokit-registry-entry-class "IOAcceleratorES")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "DeviceProperties")
+		(require-any
+			(iokit-registry-entry-class "H11ANEIn")
+			(iokit-registry-entry-class "H1xANELoadBalancer")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "ane-type")
+		(require-any
+			(iokit-registry-entry-class "AppleARMIODevice")
+			(iokit-registry-entry-class "IOPlatformExpertDevice")
+		)
 	)
 )
 
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "ANEClientHintsUserClient")
+		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
+	)
+)
 (allow iokit-open-user-client
 	(require-any
 		(iokit-connection "IOGPU")

 		(iokit-registry-entry-class "AGXCommandQueue")
 		(iokit-registry-entry-class "AGXDevice")
 		(iokit-registry-entry-class "AGXSharedUserClient")
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDeviceUserClient")
+		(iokit-registry-entry-class "H11ANEInDirectPathClient")
+		(iokit-registry-entry-class "H1xANELoadBalancerDirectPathClient")
 		(iokit-registry-entry-class "IOAccelContext")
 		(iokit-registry-entry-class "IOAccelContext2")
 		(iokit-registry-entry-class "IOAccelDevice")

 	)
 )
 
+(allow iokit-open-service
+	(require-any
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
+		(iokit-registry-entry-class "H11ANEIn")
+		(iokit-registry-entry-class "H1xANELoadBalancer")
+	)
+)
+
+(allow iokit-set-properties
+	(require-all
+		(iokit-registry-entry-class "ANEClientHintsUserClient")
+		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
+		(require-any
+			(iokit-property "ANEHintClientSessionStart")
+			(iokit-property "ANEHintClientSessionStop")
+		)
+	)
+)
+
 (allow isp-command-send)
 
 (deny job-creation)

 
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.appleneuralengine")
 		(global-name "com.apple.cvmsServ")
 		(global-name "com.apple.gpumemd.source")
 		(xpc-service-name "com.apple.AGXCompilerService*")
```
