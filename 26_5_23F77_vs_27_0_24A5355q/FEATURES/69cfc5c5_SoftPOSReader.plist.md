## SoftPOSReader.plist

> `Domain/SoftPOSReader.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>EnableOTAV3Endpoint</key>
+	<key>EnableKernelManagerV2</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>EnableOasisAppletV2</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>

```
