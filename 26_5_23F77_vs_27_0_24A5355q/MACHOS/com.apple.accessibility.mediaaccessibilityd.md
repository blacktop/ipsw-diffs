## com.apple.accessibility.mediaaccessibilityd

> `/System/Library/Frameworks/MediaAccessibility.framework/XPCServices/com.apple.accessibility.mediaaccessibilityd.xpc/com.apple.accessibility.mediaaccessibilityd`

```diff

-225.1.0.0.0
-  __TEXT.__text: 0x15d0
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__cstring: 0x2a5
-  __TEXT.__oslogstring: 0xa0
-  __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0xe2
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__cfstring: 0x200
+234.0.0.0.0
+  __TEXT.__text: 0x2cec
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_stubs: 0x280
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__cstring: 0x48e
+  __TEXT.__oslogstring: 0x5ba
+  __TEXT.__dlopen_cstrs: 0xa1
+  __TEXT.__objc_methname: 0x167
+  __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x70
-  __DATA.__bss: 0x28
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__got: 0xc8
+  __DATA.__objc_selrefs: 0xa0
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA10E1FC-85C1-3872-A23B-C4867F83AFA2
-  Functions: 30
-  Symbols:   102
-  CStrings:  64
+  UUID: 7B1DF194-A85D-3936-8D21-17CF2B072A5C
+  Functions: 66
+  Symbols:   119
+  CStrings:  123
 
Symbols:
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _SecTaskCopySigningIdentifier
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ __os_log_debug_impl
+ _abort_report_np
+ _dlerror
+ _dlsym
+ _kCFAllocatorDefault
+ _objc_release
+ _objc_release_x21
+ _objc_release_x25
+ _objc_retain
+ _os_log_create
+ _xpc_connection_get_pid
+ _xpc_release
CStrings:
+ "%s"
+ "%{public}s: explicit bundleID=%{public}@ rejected: caller=%{public}@ (pid=%d) lacks %{public}s entitlement"
+ "%{public}s: explicit bundleID=%{public}@ rejected: invalid characters (pid=%d)"
+ "%{public}s: storageMode=Global (pid=%d)"
+ "%{public}s: storageMode=Global, ignoring explicit bundleID=%{public}@, using global key (caller=%{public}@ pid=%d)"
+ "%{public}s: storageMode=PerApp, could not derive bundleID for pid=%d, falling back to global key"
+ "%{public}s: storageMode=PerApp, derivedBundleID=%{public}@ (pid=%d)"
+ "%{public}s: storageMode=PerApp, explicit bundleID=%{public}@ (caller=%{public}@ pid=%d)"
+ "."
+ "<unknown>"
+ "@\"NSString\"8@?0"
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-_"
+ "AlwaysOn"
+ "Automatic"
+ "CPCopyBundleIdentifierAndTeamFromAuditToken"
+ "CPCopyBundleIdentifierFromAuditToken"
+ "DisplayType"
+ "ForcedOnly"
+ "GET"
+ "GET global: stored value %ld is out of range [0,3], ignoring"
+ "GET global: stored value has unexpected type, ignoring"
+ "GET per-app bundleID=%{public}@: found value=%{public}s (%ld)"
+ "GET per-app bundleID=%{public}@: stored value %ld is out of range [0,3], ignoring"
+ "GET per-app bundleID=%{public}@: stored value has unexpected type, ignoring"
+ "Global"
+ "MACaptionDisplayTypeForBundleID-"
+ "MACaptionDisplayTypeStorage"
+ "MACaptionPreferAccessibleCaptions"
+ "PerApp"
+ "SET"
+ "SET global: invalid value type, ignoring"
+ "SET per-app bundleID=%{public}@: clearing key"
+ "SET per-app bundleID=%{public}@: invalid value type, ignoring"
+ "SET per-app bundleID=%{public}@: value=%{public}s (%ld)"
+ "Undefined"
+ "_migrateDisplayTypeStorageIfNeeded: persisted default storageMode=%ld (%{public}s), preferAccessibleCaptions=%d"
+ "application-identifier"
+ "bundleID"
+ "characterSetWithCharactersInString:"
+ "com.apple.application-identifier"
+ "com.apple.private.mediaAccessibility.customBundle"
+ "i"
+ "invertedSet"
+ "mediaaccessibilityd: cannot get bundle ID from audit token"
+ "migrateSettingsIfNeeded"
+ "rangeOfCharacterFromSet:"
+ "rangeOfString:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport"
+ "stringByAppendingString:"
+ "substringFromIndex:"

```
