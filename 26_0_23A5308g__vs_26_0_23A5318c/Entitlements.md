## 🔑 Entitlements

### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 		<key>com.apple.productkit.personalization</key>
 		<string>com.apple.productkit.personalization</string>
 	</dict>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```
### GameTrampoline

> `/Applications/GameTrampoline.app/GameTrampoline`

```diff

 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GameTrampoline</string>
 	<key>com.apple.developer.associated-domains</key>
-	<array>
-		<string>applinks:games.apple.com</string>
-	</array>
+	<array/>
 	<key>com.apple.developer.game-center</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key> com.apple.sharing.Session</key>
-	<true/>
 	<key>CARAppHidden</key>
 	<true/>
 	<key>CARCapableApp</key>

 		<string>com.apple.mediaremoteui</string>
 		<string>com.apple.Accessibility</string>
 	</array>
+	<key>com.apple.sharing.Session</key>
+	<true/>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction.iPhone</string>
+		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction.iPad</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.iconTintColor</key>
 	<true/>
 	<key>com.apple.springboard.lookupFolderPathForIcon</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
+	<key>com.apple.private.hid.client.admin</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-filter</key>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<array>
 		<string>com.apple.commandandcontrol</string>
 	</array>
+	<key>com.apple.realitysimulation.render-on-top-spi</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.audio.SystemSoundServer-iOS</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.SpringBoard.ReadyForRestore</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.keyboard.DictationInfoIsOnScreen</key>
 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.purplebuddy.launchMigrationSourceUI</key>

```
### AVCPlugin

> `/System/Library/ExtensionKit/Extensions/AVCPlugin.appex/AVCPlugin`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

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
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
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
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
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
	<key>com.apple.developer.hardened-process</key>
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
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
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
	<key>com.apple.developer.hardened-process</key>
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
		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
		<string>com.apple.coreservices.launchservices.session.*</string>
		<string>user.uid.501.syslog.*</string>
		<string>_AXNotification__UUID_</string>
		<string>_AXNotification_AXMRInvertColors</string>
		<string>_AXNotification_AXMRReduceWhitePoint</string>
		<string>_AXNotification_AXMuseDisplayFiltersEnabled</string>
		<string>_UUID_.notification</string>
		<string>CPActiveCountryCodeChanged.Internal</string>
		<string>MCManagedBooksChanged</string>
		<string>PINPolicyChangedNotification</string>
		<string>com.apple.ManagedConfiguration.diagnosticsCollected</string>
		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
		<string>com.apple.accessibility.QuickSpeakLocaleForLanguage</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.haptics.active.status.private</string>
		<string>com.apple.accessibility.internal.reader.changed</string>
		<string>com.apple.coreaudio.audioanalytics.tailspin.defaultsChanged</string>
		<string>com.apple.managedconfiguration._UUID_</string>
		<string>com.apple.managedconfiguration.allowhealthdatasubmissionchanged</string>
		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
		<string>com.apple.managedconfiguration.clearpasscodegenerationcaches</string>
		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
		<string>com.apple.managedconfiguration.defaultsdidchange</string>
		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
		<string>com.apple.managedconfiguration.homescreenlayoutchanged</string>
		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
		<string>com.apple.managedconfiguration.newssettingschanged</string>
		<string>com.apple.managedconfiguration.passcodechanged</string>
		<string>com.apple.managedconfiguration.restrictionchanged</string>
		<string>com.apple.managedconfiguration.settingschanged</string>
		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
		<string>com.apple.mobile.keybagd.lock_status</string>
		<string>com.apple.mobile.keybagd.user_changed</string>
		<string>com.apple.system.console_mode_changed</string>
		<string>com.apple.system.thermalpressurelevel</string>
		<string>com.apple.voiceovertouch.screencurtain</string>
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
		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
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
		<string>com.apple.WebKit.dumpAccessibilityTreeToStderr</string>
		<string>com.apple.WebKit.showGraphicsLayerTree</string>
		<string>com.apple.WebKit.showLayerTree</string>
		<string>com.apple.WebKit.showLayoutTree</string>
		<string>com.apple.WebKit.showLegacyFlexReasons</string>
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
		<string>org.WebKit.testNotification</string>
	</array>
	<key>com.apple.private.disable-log-mach-ports</key>
	<true/>
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
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>EnableQuickLookSandboxResources</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
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
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
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
	<key>com.apple.developer.hardened-process</key>
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
		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
		<string>com.apple.coreservices.launchservices.session.*</string>
		<string>user.uid.501.syslog.*</string>
		<string>_AXNotification__UUID_</string>
		<string>_AXNotification_AXMRInvertColors</string>
		<string>_AXNotification_AXMRReduceWhitePoint</string>
		<string>_AXNotification_AXMuseDisplayFiltersEnabled</string>
		<string>_UUID_.notification</string>
		<string>CPActiveCountryCodeChanged.Internal</string>
		<string>MCManagedBooksChanged</string>
		<string>PINPolicyChangedNotification</string>
		<string>com.apple.ManagedConfiguration.diagnosticsCollected</string>
		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
		<string>com.apple.accessibility.QuickSpeakLocaleForLanguage</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.haptics.active.status.private</string>
		<string>com.apple.accessibility.internal.reader.changed</string>
		<string>com.apple.coreaudio.audioanalytics.tailspin.defaultsChanged</string>
		<string>com.apple.managedconfiguration._UUID_</string>
		<string>com.apple.managedconfiguration.allowhealthdatasubmissionchanged</string>
		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
		<string>com.apple.managedconfiguration.clearpasscodegenerationcaches</string>
		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
		<string>com.apple.managedconfiguration.defaultsdidchange</string>
		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
		<string>com.apple.managedconfiguration.homescreenlayoutchanged</string>
		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
		<string>com.apple.managedconfiguration.newssettingschanged</string>
		<string>com.apple.managedconfiguration.passcodechanged</string>
		<string>com.apple.managedconfiguration.restrictionchanged</string>
		<string>com.apple.managedconfiguration.settingschanged</string>
		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
		<string>com.apple.mobile.keybagd.lock_status</string>
		<string>com.apple.mobile.keybagd.user_changed</string>
		<string>com.apple.system.console_mode_changed</string>
		<string>com.apple.system.thermalpressurelevel</string>
		<string>com.apple.voiceovertouch.screencurtain</string>
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
		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
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
		<string>com.apple.WebKit.dumpAccessibilityTreeToStderr</string>
		<string>com.apple.WebKit.showGraphicsLayerTree</string>
		<string>com.apple.WebKit.showLayerTree</string>
		<string>com.apple.WebKit.showLayoutTree</string>
		<string>com.apple.WebKit.showLegacyFlexReasons</string>
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
		<string>org.WebKit.testNotification</string>
	</array>
	<key>com.apple.private.disable-log-mach-ports</key>
	<true/>
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
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>EnableQuickLookSandboxResources</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
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
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
</dict>
</plist>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>ExternalGateway</string>
+	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>com.apple.attributionkitd.xpc.token-handoff</string>
 		<string>com.apple.backgroundassets.system</string>
 		<string>com.apple.StreamingUnzipService</string>
+		<string>com.apple.storekitd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.storekit.client-override</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

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
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
</dict>
</plist>

```

### 🆕 FamilySettings

> `/System/Library/PreferenceBundles/FamilySettings.bundle/FamilySettings`

- No entitlements *(yet)*
### AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/AppIntentsRunnerXPCService`

```diff

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
-	<key>get-task-allow</key>
-	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.modelmanager</string>
 		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.xpc.amsengagementd</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.anvil</string>
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.storeservices.itfe</string>
 	</array>

 	<string>1445028844</string>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.openai.xcode</string>
 		<string>com.apple.openai</string>
 		<string>apple</string>
 	</array>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 		<string>com.apple.Podcasts</string>
 		<string>243LU875E5.com.apple.podcasts</string>
 		<string>com.apple.MobileSMS</string>
+		<string>com.apple.GameTrampoline</string>
+		<string>com.apple.games</string>
 	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>

```
### communicationtrustd

> `/System/Library/PrivateFrameworks/CommunicationTrust.framework/Support/communicationtrustd`

```diff

 		<string>com.apple.cmfsyncagent.embedded.auth</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AppSupport</string>
+	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### CMFSyncAgent

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.cmfsyncagent</string>
+	<key>com.apple.Contacts.database-allow</key>
+	<true/>
 	<key>com.apple.StatusKit.publish.types</key>
 	<array>
 		<string>com.apple.focus.status</string>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/</string>
+		<string>/private/var/mobile/Library/AddressBook/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.StatusKit.publish</string>

 	<array>
 		<string>com.apple.cmfsyncagent</string>
 	</array>
+	<key>com.apple.security.ts.addressbook</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 </dict>

```

### 🆕 DeviceRecoveryBrainSupport

> `/System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport`

- No entitlements *(yet)*

### 🆕 LogArchiveDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LogArchiveDiagnosticExtension.appex/LogArchiveDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### intentrecommendd

> `/System/Library/PrivateFrameworks/IntentRecommendRuntime.framework/intentrecommendd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.intents.extension.discovery</key>
+	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>

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
### NewsScoringService

> `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService`

```diff

 	<array>
 		<string>group.com.apple.newsd</string>
 		<string>group.com.apple.stocks</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<integer>4201635476</integer>
 	<key>application-identifier</key>
 	<string>com.apple.passd</string>
 	<key>aps-connection-initiate</key>

 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.passd</string>
+	<key>com.apple.developer.weatherkit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.finance.private</key>

 	<true/>
 	<key>com.apple.wallet.banner</key>
 	<true/>
+	<key>fairplay-client</key>
+	<integer>87750944</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.CredentialSharingService</string>

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
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.appconduitd.allowedSPI</key>
+	<array>
+		<string>CompanionAppInfo</string>
+	</array>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

```
### ThreatNotificationCFU

> `/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/Extensions/ThreatNotificationCFU.appex/ThreatNotificationCFU`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.adid</string>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.corefollowup.agent</string>

```

### 🆕 VisualTestKit

> `/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit`

- No entitlements *(yet)*
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 		<string>group.tvappservices.container</string>
 		<string>group.com.apple.sports</string>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.visioncompaniond</string>
 		<string>com.apple.itunescloudd.xpc</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.feature-setting.allowFindMyCar</key>
 	<true/>
+	<key>com.apple.maps.assertions</key>
+	<true/>
 	<key>com.apple.maps.ipc-access</key>
 	<true/>
 	<key>com.apple.maps.model-access</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>H11ANEInDirectPathClient</string>
 		<string>AppleVirtIONeuralEngineDeviceUserClient</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```

### 🆕 libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

- No entitlements *(yet)*

### 🆕 libMTLHud.dylib

> `/usr/lib/libMTLHud.dylib`

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

### 🆕 libramrod.dylib

> `/usr/lib/libramrod.dylib`

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
### airplayd

> `/usr/libexec/airplayd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceWillow</string>

 	<array>
 		<string>/Library/Audio/Plug-Ins/HAL/</string>
 		<string>/private/var/preferences/SystemConfiguration/preferences.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.SoundProfileAsset</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

 		<string>/usr/libexec</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.mediaremote.plist</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### companiond

> `/usr/libexec/companiond`

```diff

 		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.SystemConfiguration.configd</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.tvremotecore.xpc</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-call-capabilities</string>
+	</array>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```
