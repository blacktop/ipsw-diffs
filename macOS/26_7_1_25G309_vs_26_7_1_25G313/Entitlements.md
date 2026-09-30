## 🔑 Entitlements

### filesystem

### XPCAcmeService

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/XPCAcmeService.xpc/Contents/MacOS/XPCAcmeService`

```diff

 	<string>com.apple.security.XPCAcmeService</string>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>platform-application</key>

```
### XPCAcmeService

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/XPCAcmeService.xpc/Contents/MacOS/XPCAcmeService`

```diff

 	<string>com.apple.security.XPCAcmeService</string>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>platform-application</key>

```
### uarpd

> `/usr/libexec/uarpd`

```diff

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.uarpassetmanager.uarp</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocation</key>
+	<true/>
+	<key>com.apple.security.hardened-processs.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>
 	<true/>
 	<key>com.apple.uarpassetmanager.uarp</key>

```

### 🆕 appleh13camerad

> `/usr/sbin/appleh13camerad`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.photondetector.iokit-user-access</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.cmio.extension.configuration</key>
	<true/>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleH13CamInUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>H1xANELoadBalancerDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOSurfaceRootUserClient</string>
		<string>VADResourceArbiterUserClient</string>
		<string>ApplePhotonDetectorUserClient</string>
		<string>IOUserClient</string>
	</array>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.systemstatus.publisher.domains</key>
	<array>
		<string>media</string>
	</array>
</dict>
</plist>

```


