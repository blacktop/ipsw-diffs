## Siri.plist

> `Domain/Siri.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>ASROnByDefault</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>CompositionResolution</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>asr_euclid_entity_retrieval</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>asr_jr_entity_ranking</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>assisted_linwood</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>assisted_linwood_voice_response_from_companion</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>audio_homepod_app_prediction</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>dictation_auto_punctuation_setting_enabled</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>dictation_combined_euclid_and_asr_alternatives</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>dictation_on_ifp</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>dictation_on_srd</key>
 	<dict>
 		<key>Enabled</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>proximity_user_enrollment</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>scda_framework</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>thoughtful_announce</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>trial_dictation_asset_delivery</key>
 	<dict>
 		<key>Enabled</key>

```
