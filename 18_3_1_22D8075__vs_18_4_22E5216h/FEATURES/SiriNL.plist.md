## SiriNL.plist

> `Domain/SiriNL.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>NLRouterOverrides</key>
+	<key>NLRouterAllowRoutingToGenAIGlobal</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
-	<key>NLRouterQueryDecorationIntegration</key>
+	<key>NLRouterOverrides</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>NLRouterReferenceResolution</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
 	<key>NLRouterUpdatableCorrection</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```
