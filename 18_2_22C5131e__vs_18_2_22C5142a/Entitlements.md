## 🔑 Entitlements

### AppProtectionUIHost

> `/Applications/AppProtectionUIHost.app/AppProtectionUIHost`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.seserviced.contactlessCredential.settings</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### PeopleViewService

> `/Applications/PeopleViewService.app/PeopleViewService`

```diff

 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.spotlightui</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.people</string>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.lockup-buy-params</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents.media-client-id</key>
 	<string>com.apple.searchui</string>
 	<key>com.apple.private.appstorecomponents.media-client-version</key>

 		<string>UIStatusBarStyleOverrideFullScreenWebRTCCapture</string>
 		<string>UIStatusBarStyleOverrideFullScreenWebRTCAudioCapture</string>
 	</array>
+	<key>com.apple.springboard.swapIconsInProminentPositions</key>
+	<true/>
 	<key>com.apple.springboard.webClipService</key>
 	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.contactsui</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```

### 🆕 Bookmarks

> `/System/Library/Accounts/DataclassOwners/Bookmarks.bundle/Bookmarks`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.ids</string>
 		<string>com.apple.PrototypeTools</string>
+		<string>com.apple.camera</string>
 		<string>com.apple.Bridge</string>
 		<string>/var/preferences/com.apple.networkextension.control</string>
 		<string>com.apple.TelephonyUtilities</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.SpringBoard.ReadyForRestore</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.0191488e-ff8a-728d-a9f7-08a0a77abd7d.update.client-identifiers</key>

```

### 🆕 com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.WebKit.GPU</string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.rendering</key>
	<true/>
	<key>com.apple.mediaremote.external-artwork-validation</key>
	<true/>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.mediaremote.ui-control</key>
	<true/>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.attribution.explicitly-assumed-identities</key>
	<array>
		<dict>
			<key>type</key>
			<string>wildcard</string>
		</dict>
	</array>
	<key>com.apple.private.avfoundation.capture.temporary.no-media-environment.allow</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.mediaexperience.processassertionaudittokens.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.recordingWebsite.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>
	<true/>
	<key>com.apple.private.memory.ownership_transfer</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.web-browser-engine.gpu</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.systemstatus.activityattribution</string>
	</array>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
	<key>com.apple.springboard.statusbarstyleoverrides</key>
	<true/>
	<key>com.apple.springboard.statusbarstyleoverrides.coordinator</key>
	<array>
		<string>UIStatusBarStyleOverrideWebRTCAudioCapture</string>
		<string>UIStatusBarStyleOverrideWebRTCCapture</string>
	</array>
	<key>com.apple.systemstatus.activityattribution</key>
	<true/>
	<key>com.apple.tcc.delegated-services</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.WebKit.Networking</string>
	<key>com.apple.das.private.bgtask.continuedprocessing</key>
	<true/>
	<key>com.apple.das.private.bgtask.continuedprocessing.iconBundleIdentifier</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.networking</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.private.accounts.bundleidspoofing</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>InstallWebAttribution</string>
	</array>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.WebContentRestrictions</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.ciphermld.allow</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>
		<string>kTCCServiceUserTracking</string>
	</array>
	<key>com.apple.private.web-browser-engine.network</key>
	<true/>
	<key>com.apple.private.webkit.adattributiond</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.private.webkit.webpush</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
	<key>com.apple.symptom_analytics.configure</key>
	<true/>
</dict>
</plist>

```

### 🆕 PhotosAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>com.apple.VideoSubscriberAccount.DeveloperService</key>
 	<true/>
 	<key>com.apple.VideoSubscriberAccount.PrivacyService</key>

 	<array>
 		<string>com.apple.VideoSubscriberAccount.PrivacyService</string>
 		<string>com.apple.VideoSubscriberAccount.DeveloperService</string>
+		<string>com.apple.adid</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.restrict.notifyd</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.imageio.allowabletypes</key>
	<array>
		<string>org.webmproject.webp</string>
		<string>public.jpeg</string>
		<string>public.png</string>
		<string>com.compuserve.gif</string>
	</array>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>WebContent</string>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.darwin-notification.introspect</key>
	<array>
		<string>com.apple.accessibility.cache.app.ax</string>
		<string>com.apple.accessibility.cache.ast</string>
		<string>com.apple.accessibility.cache.automation.localized.lookup</string>
		<string>com.apple.accessibility.cache.ax</string>
		<string>com.apple.accessibility.cache.captioning</string>
		<string>com.apple.accessibility.cache.differentiate.without.color</string>
		<string>com.apple.accessibility.cache.enhance.background.contrast</string>
		<string>com.apple.accessibility.cache.enhance.text.legibility</string>
		<string>com.apple.accessibility.cache.enhance.text.legibilitycom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.cache.guided.access.via.mdm</string>
		<string>com.apple.accessibility.cache.hearing.aid.paired</string>
		<string>com.apple.accessibility.cache.internal.reportvalidationerrors</string>
		<string>com.apple.accessibility.cache.invert.colors</string>
		<string>com.apple.accessibility.cache.invert.colorscom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.loc.caption.mode.enabled</string>
		<string>com.apple.accessibility.cache.mono.audio</string>
		<string>com.apple.accessibility.cache.quick.speak</string>
		<string>com.apple.accessibility.cache.reduce.motion</string>
		<string>com.apple.accessibility.cache.reduce.motion.reduce.slide.transitions</string>
		<string>com.apple.accessibility.cache.reduce.motioncom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.speak.this</string>
		<string>com.apple.accessibility.cache.speech.settings.disabled.by.mc</string>
		<string>com.apple.accessibility.cache.switch.control</string>
		<string>com.apple.accessibility.cache.vot</string>
		<string>com.apple.accessibility.cache.zoom</string>
		<string>com.apple.accessibility.cache.*</string>
		<string>com.apple.coreservices.launchservices.session.*</string>
		<string>user.uid.501.syslog.*</string>
		<string>_UUID_.notification</string>
		<string>CPActiveCountryCodeChanged.Internal</string>
		<string>MCManagedBooksChanged</string>
		<string>PINPolicyChangedNotification</string>
		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
		<string>com.apple.managedconfiguration._UUID_</string>
		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
		<string>com.apple.managedconfiguration.defaultsdidchange</string>
		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
		<string>com.apple.managedconfiguration.newssettingschanged</string>
		<string>com.apple.managedconfiguration.passcodechanged</string>
		<string>com.apple.managedconfiguration.restrictionchanged</string>
		<string>com.apple.managedconfiguration.settingschanged</string>
		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
		<string>com.apple.mobile.keybagd.lock_status</string>
		<string>com.apple.mobile.keybagd.user_changed</string>
		<string>com.apple.system.thermalpressurelevel</string>
		<string>__ABDataBaseChangedByOtherProcessNotification</string>
		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>
		<string>_AXNotification_UseNewAXBundleLoader</string>
		<string>_AXNotification_shouldPerformValidationsAtRuntime</string>
		<string>_NS_ctasd</string>
		<string>AppleCarPlayPreferredContentSizeCategoryChangedNotification</string>
		<string>AppleDatePreferencesChangedNotification</string>
		<string>AppleKeyboardsContinuousPathSettingsChangedNotification</string>
		<string>AppleKeyboardsInputModeChangedNotification</string>
		<string>AppleKeyboardsInternalSettingsChangedNotification</string>
		<string>AppleKeyboardsPreferencesChangedNotification</string>
		<string>AppleKeyboardsSettingsChangedNotification</string>
		<string>AppleLanguagePreferencesChangedNotification</string>
		<string>AppleMeasurementSystemPreferencesChangedNotification</string>
		<string>AppleNumberPreferencesChangedNotification</string>
		<string>ApplePreferredContentSizeCategoryChangedNotification</string>
		<string>AppleTemperatureUnitPreferencesChangedNotification</string>
		<string>AppleTextBehaviorPreferencesChangedNotification</string>
		<string>AppleTimePreferencesChangedNotification</string>
		<string>CPHomeCountryCodeChanged.Internal</string>
		<string>GSEventHardwareKeyboardAttached</string>
		<string>LetterFeedbackEnabled.notification</string>
		<string>PhoneticFeedbackEnabled.notification</string>
		<string>QuickTypePredictionFeedbackEnabled.notification</string>
		<string>WordFeedbackEnabled.notification</string>
		<string>com.apple.AddressBook.PreferenceChanged</string>
		<string>com.apple.CFNetwork.har-capture-update</string>
		<string>com.apple.CFPreferences._domainsChangedExternally</string>
		<string>com.apple.LaunchServices.database</string>
		<string>com.apple.UIKit.LoggingPreferences</string>
		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
		<string>com.apple.WebKit.deleteAllCode</string>
		<string>com.apple.WebKit.dumpGCHeap</string>
		<string>com.apple.WebKit.dumpUntrackedMallocs</string>
		<string>com.apple.WebKit.fullGC</string>
		<string>com.apple.WebKit.logMemStats</string>
		<string>com.apple.WebKit.logPageState</string>
		<string>com.apple.WebKit.showAllDocuments</string>
		<string>com.apple.WebKit.showBackForwardCache</string>
		<string>com.apple.WebKit.showGraphicsLayerTree</string>
		<string>com.apple.WebKit.showLayerTree</string>
		<string>com.apple.WebKit.showLayoutTree</string>
		<string>com.apple.WebKit.showMemoryCache</string>
		<string>com.apple.WebKit.showPaintOrderTree</string>
		<string>com.apple.WebKit.showRenderTree</string>
		<string>com.apple.accessibility.api</string>
		<string>com.apple.accessibility.defaultrouteforcall</string>
		<string>com.apple.accessibility.wob.status</string>
		<string>com.apple.analyticsd.running</string>
		<string>com.apple.asl.remote</string>
		<string>com.apple.caulk.alloc.audiodump</string>
		<string>com.apple.caulk.alloc.rtdump</string>
		<string>com.apple.coreaudio.list_components</string>
		<string>com.apple.coreui.statistics</string>
		<string>com.apple.distnote.locale_changed</string>
		<string>com.apple.language.changed</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mediaaccessibility.captionAppearanceSettingsChanged</string>
		<string>com.apple.powerlog.state_changed</string>
		<string>com.apple.preferences.sounds.keyboard-audio.changed</string>
		<string>com.apple.runningboard.daemonstartup</string>
		<string>com.apple.system.logging.prefschanged</string>
		<string>com.apple.system.lowpowermode</string>
		<string>com.apple.system.networkd.settings</string>
		<string>com.apple.system.syslog.master</string>
		<string>com.apple.system.timezone</string>
		<string>com.apple.system.timezone./var/db/timezone/zoneinfo/UTC</string>
		<string>com.apple.webinspectord.automatic_inspection_enabled</string>
		<string>com.apple.webinspectord.available</string>
		<string>com.apple.zoomwindow</string>
		<string>kAFPreferencesDidChangeDarwinNotification</string>
		<string>org.WebKit.lowMemory</string>
		<string>org.WebKit.lowMemory.begin</string>
		<string>org.WebKit.lowMemory.end</string>
		<string>org.WebKit.memoryWarning</string>
		<string>org.WebKit.memoryWarning.begin</string>
		<string>org.WebKit.memoryWarning.end</string>
	</array>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>EnableQuickLookSandboxResources</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
	</array>
	<key>com.apple.private.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.private.webinspector.allow-remote-inspection</key>
	<true/>
	<key>com.apple.private.webinspector.proxy-application</key>
	<true/>
	<key>com.apple.private.webkit.lockdown-mode</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.cs.allow-jit</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.restrict.notifyd</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>WebContent</string>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.darwin-notification.introspect</key>
	<array>
		<string>com.apple.accessibility.cache.app.ax</string>
		<string>com.apple.accessibility.cache.ast</string>
		<string>com.apple.accessibility.cache.automation.localized.lookup</string>
		<string>com.apple.accessibility.cache.ax</string>
		<string>com.apple.accessibility.cache.captioning</string>
		<string>com.apple.accessibility.cache.differentiate.without.color</string>
		<string>com.apple.accessibility.cache.enhance.background.contrast</string>
		<string>com.apple.accessibility.cache.enhance.text.legibility</string>
		<string>com.apple.accessibility.cache.enhance.text.legibilitycom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.cache.guided.access.via.mdm</string>
		<string>com.apple.accessibility.cache.hearing.aid.paired</string>
		<string>com.apple.accessibility.cache.internal.reportvalidationerrors</string>
		<string>com.apple.accessibility.cache.invert.colors</string>
		<string>com.apple.accessibility.cache.invert.colorscom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.loc.caption.mode.enabled</string>
		<string>com.apple.accessibility.cache.mono.audio</string>
		<string>com.apple.accessibility.cache.quick.speak</string>
		<string>com.apple.accessibility.cache.reduce.motion</string>
		<string>com.apple.accessibility.cache.reduce.motion.reduce.slide.transitions</string>
		<string>com.apple.accessibility.cache.reduce.motioncom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.speak.this</string>
		<string>com.apple.accessibility.cache.speech.settings.disabled.by.mc</string>
		<string>com.apple.accessibility.cache.switch.control</string>
		<string>com.apple.accessibility.cache.vot</string>
		<string>com.apple.accessibility.cache.zoom</string>
		<string>com.apple.accessibility.cache.*</string>
		<string>com.apple.coreservices.launchservices.session.*</string>
		<string>user.uid.501.syslog.*</string>
		<string>_UUID_.notification</string>
		<string>CPActiveCountryCodeChanged.Internal</string>
		<string>MCManagedBooksChanged</string>
		<string>PINPolicyChangedNotification</string>
		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
		<string>com.apple.managedconfiguration._UUID_</string>
		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
		<string>com.apple.managedconfiguration.defaultsdidchange</string>
		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
		<string>com.apple.managedconfiguration.newssettingschanged</string>
		<string>com.apple.managedconfiguration.passcodechanged</string>
		<string>com.apple.managedconfiguration.restrictionchanged</string>
		<string>com.apple.managedconfiguration.settingschanged</string>
		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
		<string>com.apple.mobile.keybagd.lock_status</string>
		<string>com.apple.mobile.keybagd.user_changed</string>
		<string>com.apple.system.thermalpressurelevel</string>
		<string>__ABDataBaseChangedByOtherProcessNotification</string>
		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>
		<string>_AXNotification_UseNewAXBundleLoader</string>
		<string>_AXNotification_shouldPerformValidationsAtRuntime</string>
		<string>_NS_ctasd</string>
		<string>AppleCarPlayPreferredContentSizeCategoryChangedNotification</string>
		<string>AppleDatePreferencesChangedNotification</string>
		<string>AppleKeyboardsContinuousPathSettingsChangedNotification</string>
		<string>AppleKeyboardsInputModeChangedNotification</string>
		<string>AppleKeyboardsInternalSettingsChangedNotification</string>
		<string>AppleKeyboardsPreferencesChangedNotification</string>
		<string>AppleKeyboardsSettingsChangedNotification</string>
		<string>AppleLanguagePreferencesChangedNotification</string>
		<string>AppleMeasurementSystemPreferencesChangedNotification</string>
		<string>AppleNumberPreferencesChangedNotification</string>
		<string>ApplePreferredContentSizeCategoryChangedNotification</string>
		<string>AppleTemperatureUnitPreferencesChangedNotification</string>
		<string>AppleTextBehaviorPreferencesChangedNotification</string>
		<string>AppleTimePreferencesChangedNotification</string>
		<string>CPHomeCountryCodeChanged.Internal</string>
		<string>GSEventHardwareKeyboardAttached</string>
		<string>LetterFeedbackEnabled.notification</string>
		<string>PhoneticFeedbackEnabled.notification</string>
		<string>QuickTypePredictionFeedbackEnabled.notification</string>
		<string>WordFeedbackEnabled.notification</string>
		<string>com.apple.AddressBook.PreferenceChanged</string>
		<string>com.apple.CFNetwork.har-capture-update</string>
		<string>com.apple.CFPreferences._domainsChangedExternally</string>
		<string>com.apple.LaunchServices.database</string>
		<string>com.apple.UIKit.LoggingPreferences</string>
		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
		<string>com.apple.WebKit.deleteAllCode</string>
		<string>com.apple.WebKit.dumpGCHeap</string>
		<string>com.apple.WebKit.dumpUntrackedMallocs</string>
		<string>com.apple.WebKit.fullGC</string>
		<string>com.apple.WebKit.logMemStats</string>
		<string>com.apple.WebKit.logPageState</string>
		<string>com.apple.WebKit.showAllDocuments</string>
		<string>com.apple.WebKit.showBackForwardCache</string>
		<string>com.apple.WebKit.showGraphicsLayerTree</string>
		<string>com.apple.WebKit.showLayerTree</string>
		<string>com.apple.WebKit.showLayoutTree</string>
		<string>com.apple.WebKit.showMemoryCache</string>
		<string>com.apple.WebKit.showPaintOrderTree</string>
		<string>com.apple.WebKit.showRenderTree</string>
		<string>com.apple.accessibility.api</string>
		<string>com.apple.accessibility.defaultrouteforcall</string>
		<string>com.apple.accessibility.wob.status</string>
		<string>com.apple.analyticsd.running</string>
		<string>com.apple.asl.remote</string>
		<string>com.apple.caulk.alloc.audiodump</string>
		<string>com.apple.caulk.alloc.rtdump</string>
		<string>com.apple.coreaudio.list_components</string>
		<string>com.apple.coreui.statistics</string>
		<string>com.apple.distnote.locale_changed</string>
		<string>com.apple.language.changed</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mediaaccessibility.captionAppearanceSettingsChanged</string>
		<string>com.apple.powerlog.state_changed</string>
		<string>com.apple.preferences.sounds.keyboard-audio.changed</string>
		<string>com.apple.runningboard.daemonstartup</string>
		<string>com.apple.system.logging.prefschanged</string>
		<string>com.apple.system.lowpowermode</string>
		<string>com.apple.system.networkd.settings</string>
		<string>com.apple.system.syslog.master</string>
		<string>com.apple.system.timezone</string>
		<string>com.apple.system.timezone./var/db/timezone/zoneinfo/UTC</string>
		<string>com.apple.webinspectord.automatic_inspection_enabled</string>
		<string>com.apple.webinspectord.available</string>
		<string>com.apple.zoomwindow</string>
		<string>kAFPreferencesDidChangeDarwinNotification</string>
		<string>org.WebKit.lowMemory</string>
		<string>org.WebKit.lowMemory.begin</string>
		<string>org.WebKit.lowMemory.end</string>
		<string>org.WebKit.memoryWarning</string>
		<string>org.WebKit.memoryWarning.begin</string>
		<string>org.WebKit.memoryWarning.end</string>
	</array>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>EnableQuickLookSandboxResources</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
	</array>
	<key>com.apple.private.verified-jit</key>
	<true/>
	<key>com.apple.private.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.private.webinspector.allow-remote-inspection</key>
	<true/>
	<key>com.apple.private.webinspector.proxy-application</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
</dict>
</plist>

```
### contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.appprotectiond.read</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.TelephonyUtilities</string>
+	</array>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-call-providers</string>

```

### 🆕 SafariServices

> `/System/Library/Frameworks/SafariServices.framework/PlugIns/SafariServices.wkbundle/SafariServices`

- No entitlements *(yet)*

### 🆕 com.apple.SafariServices.ContentBlockerLoader

> `/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.can-load-any-content-blocker</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.safari</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/Applications/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Safari/</string>
	</array>
</dict>
</plist>

```

### 🆕 adattributiond

> `/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile</key>
	<string>com.apple.WebKit.adattributiond</string>
</dict>
</plist>

```

### 🆕 PaymentContactlessUIPlugin

> `/System/Library/PreferenceBundles/PaymentContactlessUIPlugin.bundle/PaymentContactlessUIPlugin`

- No entitlements *(yet)*
### AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.ucrt.healing.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.imagent</key>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
 	<key>com.apple.runningboard.jetengine</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.availability.internal</string>

```
### CDPFollowUpExtension

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.backboardd.replacesystemapp</key>
 	<true/>
 	<key>com.apple.businessservicesd.prefetch</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.mobile.installd</string>
+        <string>com.apple.sysdiagnose.service.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>GetSystemAppMigrationStatus</string>
 		<string>WaitForSystemAppMigrationToComplete</string>
 	</array>
+    <key>com.apple.private.sysdiagnose</key>
+    <true/>
+    <key>com.apple.security.exception.process-info</key>
+    <true/>
 </dict>
 </plist>
 

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<array>
 		<string>IntelligenceFlow.JointResolverTelemetry</string>
 		<string>IntelligenceEngine.Interaction.Donation</string>
+		<string>IntelligenceFlow.PlanResolutionTelemetry</string>
 		<string>IntelligenceFlow.QueryDecorationTelemetry</string>
 		<string>IntelligenceFlow.Telemetry</string>
 		<string>IntelligenceFlow.ResponseGeneration</string>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>App.InFocus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Autonaming.Messages.Inferences</key>
 				<dict>
 					<key>mode</key>

```

### 🆕 BrowsingDataImport

> `/System/Library/PrivateFrameworks/MobileSafari.framework/XPCServices/BrowsingDataImport.xpc/BrowsingDataImport`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.ArchiveService.XPC</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.desktopservices.ArchiveService</string>
		<string>com.apple.Safari.CredentialExtractionHelper</string>
	</array>
</dict>
</plist>

```

### 🆕 PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

- No entitlements *(yet)*

### 🆕 AutoFillHelper

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authentication-services.access-credential-identities</key>
	<true/>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.octagon</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assertiond.applicationstateconnection</string>
		<string>com.apple.SharedWebCredentials</string>
		<string>com.apple.securityd</string>
		<string>com.apple.security.octagon</string>
		<string>com.apple.accountsd.accountmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.WebUI</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.cfnetwork</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>AutoFillHelper</string>
	</array>
</dict>
</plist>

```

### 🆕 CredentialProviderExtensionHelper

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/CredentialProviderExtensionHelper.xpc/CredentialProviderExtensionHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authentication-services.access-credential-identities</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>CredentialProviderExtensionHelper</string>
	</array>
</dict>
</plist>

```

### 🆕 SafariConfigurationSubscriber

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/SafariConfigurationSubscriber.xpc/SafariConfigurationSubscriber`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.SafariShared.SafariConfigurationSubscriber</string>
	<key>com.apple.private.remotemanagement.subscriber</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.remotemanagementd.store</string>
		<string>com.apple.RemoteManagementAgent.store</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.remotemanagement.SafariSubscriber</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<array>
		<string>com.apple.SafariShared.SafariConfigurationSubscriber</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.Safari.CredentialExtractionHelper

> `/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.CredentialExtractionHelper.xpc/com.apple.Safari.CredentialExtractionHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile</key>
	<string>temporary-sandbox</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 com.apple.Safari.SearchHelper

> `/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile</key>
	<string>SafariSearchHelper</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 VisualTestKit

> `/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit`

- No entitlements *(yet)*
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	</dict>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>GetSystemAppMigrationStatus</string>
+	</array>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.mobile.installd</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.sessionservices</string>

 	<array>
 		<string>180</string>
 	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>V568VXD5P8.is.workflow.my.app</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.lsd.mapdb</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 		<string>UIStatusBarStyleOverrideWebRTCCapture</string>
 		<string>UIStatusBarStyleOverrideWebRTCAudioCapture</string>
 	</array>
+	<key>com.apple.springboard.swapIconsInProminentPositions</key>
+	<true/>
 	<key>com.apple.springboard.systemNotesPresentation</key>
 	<true/>
 	<key>com.apple.springboard.wallpaperAnimationSuspension</key>

```
### com.apple.mobilesafari.SafariDiagnosticExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension`

```diff

 	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.safari</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/CrashReporter/</string>

```

### 🆕 com.apple.Safari.SandboxBroker

> `/private/var/staged_system_apps/MobileSafari.app/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobilesafari</string>
	</dict>
	<key>com.apple.private.imcore.spi.database-access</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/SMS/Attachments/</string>
		<string>/Containers/Data/Application/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleJPEGDriverUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
		<string>com.apple.trustd</string>
		<string>com.apple.webprivacyd</string>
		<string>com.apple.symptom_diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.imessage.bag</string>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.ids</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Safari.SandboxBroker</string>
	</array>
</dict>
</plist>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>259</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```

### 🆕 libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

- No entitlements *(yet)*

### 🆕 libffi-trampolines.dylib

> `/usr/lib/libffi-trampolines.dylib`

- No entitlements *(yet)*

### 🆕 libglInterpose.dylib

> `/usr/lib/libglInterpose.dylib`

- No entitlements *(yet)*

### 🆕 libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

- No entitlements *(yet)*

### 🆕 libobjc-trampolines.dylib

> `/usr/lib/libobjc-trampolines.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.6.0.9.dylib

> `/usr/lib/libstdc++.6.0.9.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.6.dylib

> `/usr/lib/libstdc++.6.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.dylib

> `/usr/lib/libstdc++.dylib`

- No entitlements *(yet)*

### 🆕 BatteryAlgorithms

> `/usr/libexec/BatteryAlgorithms.framework/BatteryAlgorithms`

- No entitlements *(yet)*
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
+	<key>com.apple.private.kernel.jetsam</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.mako.status</key>

 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceExposureNotification</string>
 	</array>
+	<key>com.apple.private.write-kr-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.xpc.allowed-get-service-name</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.service-stats</key>

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>259</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>259</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.inputanalyticsd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>

```
### nptocompaniond

> `/usr/libexec/nptocompaniond`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.lsd.mapdb</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	</array>
 	<key>com.apple.remotemanagementd.management-state</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.safari</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/installd/Library/MobileInstallation/MigrationInfo.plist</string>

```
