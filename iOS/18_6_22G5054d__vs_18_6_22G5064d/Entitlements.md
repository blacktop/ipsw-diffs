## 🔑 Entitlements

### PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.email.maild</string>
 		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.cloudd</string>

```
