## 🔑 Entitlements


### 🆕 ConditionalEngineAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/ConditionalEngineAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.conditionalengine</string>
	<key>com.apple.CoreRoutine.LocationOfInterest</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.intelligenceflow.context</key>
	<true/>
	<key>com.apple.intelligenceflow.orchestrator</key>
	<true/>
	<key>com.apple.intelligenceflow.orchestrator.features</key>
	<array>
		<string>executable-session</string>
	</array>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework</string>
	</array>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.intelligenceflow.group-identifier</key>
	<string>com.apple.conditionalengine</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.conditionalengine</string>
	</array>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.userprofiles.read</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.conditionalengine</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siriactionsd.xpc</string>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.intelligenceflow.orchestrator</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.intelligenceflow.context</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.conditionalengine</string>
	</array>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.trigger-editing</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
</dict>
</plist>

```

### 🆕 ConditionalEngineLighthouseExtension

> `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/ConditionalEngineLighthouseExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.conditionalengine.ConditionalEngineLighthouseExtension</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 	<true/>
 	<key>com.apple.launchservices.MoveDocumentOnOpen</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.CarveoutProperty</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.AudioAnalytics</string>

 		<string>IOHIDLibUserClient</string>
 		<string>AppleSPUHIDDeviceUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.polaris.client</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.CarPlayServices.app-history</key>
 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.borealis</key>

 		<string>AppleHapticsSupportUserClient</string>
 		<string>AHSPowerInterfaceUserClient</string>
 		<string>AppleSMCClient</string>
+		<string>AppleProcessorTraceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	</array>
 	<key>com.apple.systemstatus.publisher.domains</key>
 	<string>media</string>
+	<key>com.apple.tailspin.cputrace</key>
+	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```
### tailspind

> `/usr/libexec/tailspind`

```diff

 	<true/>
 	<key>com.apple.logd.admin</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
 	<key>com.apple.private.kernel.ktrace-background</key>

 	<array>
 		<string>com.apple.tailspin.notifications</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
