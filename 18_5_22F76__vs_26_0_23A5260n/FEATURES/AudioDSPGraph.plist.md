## AudioDSPGraph.plist

> `Domain/AudioDSPGraph.plist`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict/>
+<dict>
+	<key>AudioDSPGraphFramework_AudioDSP</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>AudioDSPGraphFramework_AudioDSPManager</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>AudioDSPGraphFramework_AudioDSP_DNNVADInterface</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>AudioDSPGraphFramework_AudioDSP_UplinkSpeechMixerSPI</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>AudioDSPGraphFramework_AudioHAL</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>AudioDSPGraphFramework_CoreAudioTools</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>AudioDSPGraphFramework_VirtualAudio_NewHardwareOnly</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>AudioDSPGraphFramework_VoiceProcessor</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+</dict>
 </plist>
 

```
