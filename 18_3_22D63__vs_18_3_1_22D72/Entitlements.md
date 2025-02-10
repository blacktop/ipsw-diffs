## 🔑 Entitlements

### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	</dict>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.familycircle.agent</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.modelcatalog.catalog</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.siri.generativeassistantsettings</string>

```
### powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

 	<array>
 		<string>com.apple.powerui.bdcdata</string>
 		<string>com.apple.powerexperienced.resourceusage</string>
-		<string>com.apple.datamigrator</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
