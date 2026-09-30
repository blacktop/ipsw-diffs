## 🔑 Entitlements

### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<true/>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.hid.client.admin</key>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceCalendar</string>
 	</array>
+	<key>com.apple.private.tcc.external.report</key>
+	<true/>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.tipsd</string>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceIdentityXPCService.access</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.idcredentials.storage</key>

 	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+	</array>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>

 	<array>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.CoreSpeech</string>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<string>com.apple.VisualIntelligenceCamera</string>
 	<key>com.apple.private.payment.remote-network-payment-initiate</key>
 	<true/>
+	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>container</string>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### ShortcutsActions

> `/System/Library/CoreServices/ShortcutsActions.app/ShortcutsActions`

```diff

 	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.shortcuts</string>
+	</dict>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.keystore.absinthe</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.passd.account</key>

 		<string>com.apple.ap.promotedcontent.identifiermanager</string>
 		<string>com.apple.absd</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.keystore.absinthe</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.passd.account</key>

 		<string>com.apple.ap.promotedcontent.identifiermanager</string>
 		<string>com.apple.absd</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### contactsdonationagent

> `/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.contactsd.support</string>
+	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.sbpl</key>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coretelephony.Calls.allow</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

```
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.keystore.absinthe</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.passd.account</key>

 		<string>com.apple.ap.promotedcontent.identifiermanager</string>
 		<string>com.apple.absd</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.FailureReason</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>GenerativeExperiences.WritingToolsFeatures.ComposeAndAdjust</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 			</dict>
 		</dict>
 	</dict>

```
