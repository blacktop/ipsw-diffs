## 🔑 Entitlements


### 🆕 Bookmarks

> `/System/Library/Accounts/DataclassOwners/Bookmarks.bundle/Bookmarks`

- No entitlements *(yet)*

### 🆕 com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

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
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
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
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
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
