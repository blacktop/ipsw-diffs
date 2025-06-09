## AVConference.plist

> `Domain/AVConference.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AFB</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>AlwaysHDCapture</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>AudioREDDecayFactorABTesting</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>CompressedMoCap</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>EnableEnhancedJBAdaptationsForFTA</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>EnableEyeContactOniPad</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>EnableFrameBasedFEC</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>EnableGFTDowngradeToOneToOne</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>EnableMaxCameraBitrateVideoQualityV3</key>
+	<key>EnableHDR10DefaultNegotiation</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>EnableLateKeyFrameDetection</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>EnableMLRateController</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>EnableMTERetagging</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>EnableMaxCameraBitrateVideoQualityV4</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
 	<key>EnableMotionBasedDuplication</key>
 	<dict>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>EnableSpeechDetector</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>EnableThermalLightMitigations</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>EnableTransportMute_iOS</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>EnableTransportMute_tvOS</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>EnableTransportMute_visionOS</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>EnableTransportMute_watchOS</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>EnableUplinkRetransmissionForVideo</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>ImprovedPacketLossConcealmentAACELD</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>JBLatencySensitiveModeEnabled</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>LimitMultiwayBandwidthWhenConstrained</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>SendAACELDSBRHeaderWithEveryFrame</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>SkipNonInfraWiFiAssertion</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>UseAnalyzerSpeechAPI_iOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>UseAnalyzerSpeechAPI_macOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>UseAnalyzerSpeechAPI_tvOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>UseAnalyzerSpeechAPI_visionOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UseAudioHostTimeForAVSync</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>UseFRCForLowTierGFT</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UseHigherAudioREDCutoverForU1</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>UseLowBandwidthSinglePacketDuplication</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UseNWConnectionMonitorForVCCM</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>UseOutOfProcessAudioDecoding_visionOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UseOutOfProcessAudioDecoding_watchOS</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>UseOutOfProcessVideoDecoding_visionOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UseOutOfProcessVideoDecoding_watchOS</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>pqcU1Enabled</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 </dict>
 </plist>
 

```
