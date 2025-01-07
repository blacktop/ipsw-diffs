## 🔑 Entitlements

### MusicRecognition

> `/Applications/MusicRecognition.app/MusicRecognition`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents.media-client-id</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
-	<key>com.apple.ane.iokit-user-access</key>
-	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

```
### GenerativeAssistantExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension`

```diff

 	<array>
 		<string>/private/var/tmp/VICamera/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/SiriReferenceResolution/</string>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
 		<string>com.apple.UIKit.InternalPreferences</string>
 		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
+		<string>com.apple.accessibility.haptics.active.status.private</string>
 		<string>com.apple.managedconfiguration._UUID_</string>
 		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
 		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
 		<string>com.apple.UIKit.InternalPreferences</string>
 		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
+		<string>com.apple.accessibility.haptics.active.status.private</string>
 		<string>com.apple.managedconfiguration._UUID_</string>
 		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
 		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 		<string>IAPHistory</string>
 		<string>InstallAttribution</string>
 		<string>Ocelot</string>
+		<string>Purchase</string>
 		<string>Repair</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<true/>
 	<key>com.apple.private.MobileAsset.ManifestStorageService</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.allow-nsurlsession-proxy</key>
 	<true/>
 	<key>com.apple.private.apfs.get-graft-info</key>

```
