## SharingPrefsExtension

> `/System/Library/PrivateFrameworks/AMPSharing.framework/Versions/A/PlugIns/SharingPrefsExtension.appex/Contents/MacOS/SharingPrefsExtension`

```diff

-1.5.2.56.0
-  __TEXT.__text: 0x168938
-  __TEXT.__auth_stubs: 0x15e0
-  __TEXT.__objc_stubs: 0x8300
+1.5.4.70.0
+  __TEXT.__text: 0x1718b4
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_stubs: 0x8360
   __TEXT.__init_offsets: 0x48
-  __TEXT.__objc_methlist: 0x2a90
-  __TEXT.__gcc_except_tab: 0x8b7c
-  __TEXT.__const: 0x2b0c6
-  __TEXT.__cstring: 0x4cee
-  __TEXT.__oslogstring: 0x1ca0
+  __TEXT.__objc_methlist: 0x332c
+  __TEXT.__gcc_except_tab: 0x8e2c
+  __TEXT.__const: 0x2b1f6
+  __TEXT.__cstring: 0x4e7b
+  __TEXT.__oslogstring: 0x1eeb
   __TEXT.__objc_classname: 0x454
-  __TEXT.__objc_methname: 0xaf65
-  __TEXT.__objc_methtype: 0x1bcd
+  __TEXT.__objc_methname: 0xafd4
+  __TEXT.__objc_methtype: 0x1bd8
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x3c78
+  __TEXT.__unwind_info: 0x3dc8
   __TEXT.__eh_frame: 0xcc
-  __DATA_CONST.__auth_got: 0xb08
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x17f68
-  __DATA_CONST.__cfstring: 0x2e20
+  __DATA_CONST.__auth_got: 0xb10
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x18e80
+  __DATA_CONST.__cfstring: 0x2ec0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x220
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x5b80
-  __DATA.__objc_selrefs: 0x2808
+  __DATA.__objc_const: 0x4b00
+  __DATA.__objc_selrefs: 0x2cf0
   __DATA.__objc_ivar: 0x3cc
   __DATA.__objc_data: 0x910
-  __DATA.__data: 0x700
-  __DATA.__bss: 0x51f0
-  __DATA.__common: 0x1080
+  __DATA.__data: 0x710
+  __DATA.__bss: 0x5200
+  __DATA.__common: 0x1088
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3A44DC22-D75F-34BE-8F66-81B6C46021D4
-  Functions: 3638
-  Symbols:   581
-  CStrings:  3674
+  UUID: BBFF3296-F75C-3739-A449-D0D0B86F2DED
+  Functions: 3710
+  Symbols:   584
+  CStrings:  3708
 
Symbols:
+ _CFStringAppendCharacters
+ _CFStringCreateMutable
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
CStrings:
+ "!this->HasPendingRequests()"
+ "%26"
+ "***ERROR*** ProcessRequest could not find a request again after prepare, assuming the request has been cancelled."
+ "***ERROR*** ProcessRequest could not find a request, assuming the request has been cancelled."
+ "1.5.4"
+ "@20@0:8f16"
+ "AMPErrorDomainHRESULT"
+ "AppleWebKit"
+ "Cancelling all requests with reason %s, except those marked non-cancellable."
+ "Cancelling all requests with reason %s."
+ "Could not register StoreServices un-initialization proc. Not initialized."
+ "DMAPTagged requests have to be POST."
+ "Destroying request scheduler."
+ "ExplicitContentBadgeTreatment"
+ "Found request scheduler with pending requests at StoreServices un-initialization time."
+ "Left %lu requests uncancelled."
+ "No clientId to fetch API token."
+ "No token service! Cannot get JWT for Request %{public}s(%d)"
+ "No token service.."
+ "Notification arrived after shutdown has begun. Ignoring."
+ "Other"
+ "Pref 'log-request-to-har-path' is not present or empty."
+ "ProcesQuitting"
+ "Scheduler was destroyed. Cannot continue request %{public}s(%d) after custom requirements were satisfied."
+ "Scheduler was destroyed. Cannot set JWT in request %{public}s(%d)"
+ "Scheduler was destroyed. Cannot set Mescal session in request %{public}s(%d)"
+ "Scheduler was destroyed. Cannot set StoreBag in request %{public}s(%d)"
+ "SchedulerLocked"
+ "Stopping accepting requests."
+ "StoreServices::IsInitialized()"
+ "application/x-dmap-tagged"
+ "bundleWithIdentifier:"
+ "cancel"
+ "com.apple.amp.desktopui"
+ "glyphForVolume:"
+ "image/jpeg"
+ "imageWithSystemSymbolName:variableValue:accessibilityDescription:"
+ "isExplicitContentAgeVerificationRequired"
+ "korea"
+ "notificationRegistration"
+ "request_scheduler"
+ "speaker.wave.3.fill"
+ "urlRequest.IsValid() || error.IsValid()"
+ "videoHUD_Volume"
- " AppleWebKit/"
- "***ERROR*** Could not find a request again after prepare, assuming the request has been cancelled."
- "***ERROR*** Could not find a request, assuming the request has been cancelled."
- "1.5.2"
- "Cannot get JWT. No token service!!!"
- "Pref 'log-request-to-har-path' is not present"
- "Scheduler was destroyed. Cannot continue after custom requirements were satisfied."
- "Scheduler was destroyed. Cannot set JWT."
- "Scheduler was destroyed. Cannot set Mescal session."
- "Scheduler was destroyed. Cannot set StoreBag."
- "fullName"
- "requestscheduler"
- "this->IsSuccessful()"
- "uString != nullptr"

```
