## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-5.1.7.0.0
-  __TEXT.__text: 0x4431c
+5.2.1.1.0
+  __TEXT.__text: 0x44b08
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x2f70
+  __TEXT.__objc_methlist: 0x2f88
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0xf2c
-  __TEXT.__cstring: 0x43c8
-  __TEXT.__oslogstring: 0x4bc6
+  __TEXT.__gcc_except_tab: 0xf80
+  __TEXT.__cstring: 0x4427
+  __TEXT.__oslogstring: 0x4cff
   __TEXT.__dlopen_cstrs: 0x55
-  __TEXT.__unwind_info: 0xec0
+  __TEXT.__unwind_info: 0xed8
   __TEXT.__objc_classname: 0x61d
-  __TEXT.__objc_methname: 0xc358
+  __TEXT.__objc_methname: 0xc44a
   __TEXT.__objc_methtype: 0x1623
-  __TEXT.__objc_stubs: 0xa1a0
-  __DATA_CONST.__got: 0xff8
-  __DATA_CONST.__const: 0x1950
+  __TEXT.__objc_stubs: 0xa280
+  __DATA_CONST.__got: 0x1000
+  __DATA_CONST.__const: 0x1988
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b60
+  __DATA_CONST.__objc_selrefs: 0x2b98
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x620
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x4940
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x49c0
   __AUTH_CONST.__objc_const: 0x6648
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0xd20
   __DATA.__objc_ivar: 0x238
   __DATA.__data: 0x6c0
-  __DATA.__bss: 0x1e0
+  __DATA.__bss: 0x1f0
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1288
-  Symbols:   2208
-  CStrings:  3088
+  Functions: 1293
+  Symbols:   2216
+  CStrings:  3103
 
Symbols:
+ _MCFeatureDefaultBrowserPromptingAllowed
+ _OBJC_CLASS_$_LSApplicationRecord
+ _kMDMPSettingsDefaultApplications
CStrings:
+ "CustomSetDefaultBrowserErrorDomain"
+ "DefaultApplications"
+ "Failed to set default browser to %!{(MISSING)public}@ with error code %!{(MISSING)public}@"
+ "MDMServerCore failed to execute remote management unenrollment with error: %!{(MISSING)public}@"
+ "MDMServerCore failed to stop managing app '%!{(MISSING)public}@' with error: %!{(MISSING)public}@"
+ "MDMServerCore ignoring stop managing books with error: %!{(MISSING)public}@"
+ "MDMServerCore posting MDM uprooted notifications: %!{(MISSING)public}@"
+ "MDMServerCore uprooting MDM installation..."
+ "Setting default browser: %!{(MISSING)public}@"
+ "Successfully set the default browser. Disallowing preference prompting."
+ "WebBrowser"
+ "_performSetDefaultApplications:"
+ "_performSetDefaultBrowser:completion:"
+ "_processAccountDrivenUnauthorizedFromTransaction:rmAccountID:reauthQueue:"
+ "allowDefaultBrowserPrompting"
+ "initWithBundleIdentifier:fetchingPlaceholder:error:"
+ "isEligibleWebBrowser"
+ "isWebBrowser"
+ "setBoolValue:forSetting:"
+ "setDefaultWebBrowserToApplicationRecord:completionHandler:"
- "Could not execute remote management unenrollment, error: %!{(MISSING)public}@"
- "Could not stop managing app: %!{(MISSING)public}@, error: %!{(MISSING)public}@"
- "Ignoring stop managing books error: %!{(MISSING)public}@"
- "Uprooting MDM installation"
- "_processUserChannelUnauthorizedFromTransaction:rmAccountID:reauthQueue:"

```
