## VirtualGarage

> `/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage`

```diff

-2340.33.11.14.1
-  __TEXT.__text: 0x29950
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x17ec
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x2a59
-  __TEXT.__oslogstring: 0x464d
-  __TEXT.__gcc_except_tab: 0xf48
-  __TEXT.__unwind_info: 0x888
-  __TEXT.__objc_classname: 0x394
-  __TEXT.__objc_methname: 0x4978
-  __TEXT.__objc_methtype: 0xb7e
-  __TEXT.__objc_stubs: 0x39a0
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x1050
-  __DATA_CONST.__objc_classlist: 0x90
+2340.34.9.12.11
+  __TEXT.__text: 0x2aec4
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x1eac
+  __TEXT.__const: 0x178
+  __TEXT.__cstring: 0x2b34
+  __TEXT.__oslogstring: 0x4957
+  __TEXT.__gcc_except_tab: 0xfbc
+  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__objc_classname: 0x3ec
+  __TEXT.__objc_methname: 0x4b49
+  __TEXT.__objc_methtype: 0xbdf
+  __TEXT.__objc_stubs: 0x3b00
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x1070
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1128
+  __DATA_CONST.__objc_selrefs: 0x12d8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x13a0
-  __AUTH_CONST.__objc_const: 0x3920
+  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__objc_const: 0x31c0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x1f4
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x214
   __DATA.__data: 0x7f0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_ivar: 0x58
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__data: 0x1c0
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x80
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 706
-  Symbols:   976
-  CStrings:  1560
+  Functions: 729
+  Symbols:   1005
+  CStrings:  1610
 
Symbols:
+ _GEOCountryConfigurationCountryCodeDidChangeNotification
+ _OBJC_CLASS_$_NSMapTable
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _NSCurrentLocaleDidChangeNotification
- _fmod
CStrings:
+ "\x02\x12"
+ "\x05"
+ "-[VGOEMExtensionConnectionBroker resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:]_block_invoke"
+ "-[_VGOEMExtensionConnection initWithConnection:]_block_invoke"
+ "-[_VGOEMExtensionConnection resumeWithCompletion:]_block_invoke"
+ "<%@ %p, intent: %@, id: %@, hash: %lu>"
+ "@\"INIntent\""
+ "@\"NSMapTable\""
+ "@?"
+ "Started a new streaming Intent %@ with %@"
+ "T@\"VGOEMExtensionConnectionBroker\",R,N"
+ "VGOEMExtensionConnection"
+ "VGOEMExtensionConnectionBroker"
+ "[%{public}@] Connection has already been resumed"
+ "[%{public}p] Added new request to extension map: %@"
+ "[%{public}p] Adding connection error handler: %@"
+ "[%{public}p] Adding connection timeout handler: %@"
+ "[%{public}p] Adding intent completion handler: %@"
+ "[%{public}p] Coalescing duplicate connection request: %@"
+ "[%{public}p] Completed connection request: %@"
+ "[%{public}p] Connection timed out: %@"
+ "[%{public}p] Creating intent connection for intent (%@) with timeout (%.2f) trust check: (%ld)"
+ "[%{public}p] Deallocating"
+ "[%{public}p] Executing %lu connection error handler(s)"
+ "[%{public}p] Executing %lu connection timeout handler(s)"
+ "[%{public}p] Executing %lu intent completion handler(s)"
+ "[%{public}p] Got error resuming connection: %@"
+ "[%{public}p] Got intent response: %@, error: %@"
+ "[%{public}p] Initializing with connection: %@"
+ "[%{public}p] Received new connection request: %@"
+ "[%{public}p] Removed request from extension map: %@"
+ "[%{public}p] Resuming connection"
+ "[%{public}p] Successfully resumed connection; starting intent handling"
+ "_VGOEMExtensionConnection"
+ "_VGOEMExtensionConnectionKey"
+ "_complete"
+ "_completion"
+ "_completionLock"
+ "_connectionErrorHandlers"
+ "_connectionTimeoutHandlers"
+ "_extensionMap"
+ "_handlersLock"
+ "_intent"
+ "_intentCompletionHandlers"
+ "_lock"
+ "addConnectionErrorHandler:"
+ "addConnectionTimeoutHandler:"
+ "addIntentCompletionHandler:"
+ "carName"
+ "countryCodeDidChange:"
+ "countryCodeDidChange:, will reload networks "
+ "initWithConnection:"
+ "initWithKeyOptions:valueOptions:capacity:"
+ "launchId"
+ "objectForKey:"
+ "resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:"
+ "resumeWithCompletion:"
+ "sharedInstance"
+ "v24@?0@\"INIntentResponse\"8@\"INCExtensionError\"16"
+ "v48@0:8@16@?24@?32@?40"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\x04\x12"
- "-[VGChargingNetworkAvailabilityProvider _localeChanged:]_block_invoke"
- "-[VGChargingNetworkAvailabilityProvider initWithDelegate:]_block_invoke"
- "-[VGOEMApplication _connectionWithIntent:]_block_invoke"
- "Creating connection for OEMApp: (%@), with timeout %.2f"
- "Started a new Intent %@ with %@"
- "_activeCountryCode"
- "_activeLanguageCode"
- "_localeChanged:"
- "_localeChanged:, oldCountryCode: %@, newCountryCode: %@, oldLanguageCode: %@, newLanguageCode: %@ -> will not reload networks"
- "_localeChanged:, oldCountryCode: %@, newCountryCode: %@, oldLanguageCode: %@, newLanguageCode: %@ -> will reload networks"
- "languageCode"

```
