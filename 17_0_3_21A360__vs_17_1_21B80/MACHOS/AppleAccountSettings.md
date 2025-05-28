## AppleAccountSettings

> `/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings`

```diff

-486.1.1.4.0
-  __TEXT.__text: 0x5b1e8
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_stubs: 0xb9a0
-  __TEXT.__objc_methlist: 0x3ae0
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2e55
-  __TEXT.__objc_methname: 0xf2eb
-  __TEXT.__oslogstring: 0x5649
+493.2.1.1.0
+  __TEXT.__text: 0x5b898
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_stubs: 0xba20
+  __TEXT.__objc_methlist: 0x3af0
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x2e60
+  __TEXT.__objc_methname: 0xf331
+  __TEXT.__oslogstring: 0x5b0c
   __TEXT.__objc_classname: 0xb3f
-  __TEXT.__objc_methtype: 0x3473
-  __TEXT.__gcc_except_tab: 0x944
+  __TEXT.__objc_methtype: 0x34bc
+  __TEXT.__gcc_except_tab: 0x950
   __TEXT.__dlopen_cstrs: 0x261
-  __TEXT.__unwind_info: 0x1694
-  __DATA_CONST.__auth_got: 0x500
-  __DATA_CONST.__got: 0x5d8
+  __TEXT.__unwind_info: 0x16ac
+  __DATA_CONST.__auth_got: 0x518
+  __DATA_CONST.__got: 0x5e0
   __DATA_CONST.__const: 0x1960
   __DATA_CONST.__cfstring: 0x37e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0x11718
-  __DATA.__objc_selrefs: 0x36c0
+  __DATA.__objc_const: 0x11938
+  __DATA.__objc_selrefs: 0x36e0
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x840
   __DATA.__objc_superrefs: 0x160
-  __DATA.__objc_ivar: 0x6d0
+  __DATA.__objc_ivar: 0x6d4
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0xd80
   __DATA.__bss: 0x118

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1752
-  Symbols:   725
-  CStrings:  3776
+  Functions: 1766
+  Symbols:   730
+  CStrings:  3796
 
Symbols:
+ _CGAffineTransformIdentity
+ _CGAffineTransformRotate
+ _CGAffineTransformTranslate
+ _CGRectApplyAffineTransform
+ _OBJC_CLASS_$_NSConstantDictionary
CStrings:
+ "\x02\x12!"
+ "\x0f\x03\x11"
+ "!1"
+ "AAUIAppleAccountViewController (%@) did receieve objectModel (%@) with actionSignal (%lu)"
+ "AAUIAppleAccountViewController dealloc"
+ "AAUIAppleAccountViewController missing reference for AADeviceLocatorStateDidChangeNotification"
+ "AAUIAppleAccountViewController observed AADeviceLocatorStateDidChangeNotification"
+ "AAUIAppleAccountViewController: Undefined action signal and no page, not displaying modally! Processing objectModel (%@) with handler (%@)"
+ "AAUICDPSpecifierProvider: adp is enabled - reloading specifiers"
+ "AAUIDataclassViewController Failed to load %{public}@ from bundle: %{public}@"
+ "AAUIMainSettingsViewController _accountDidChangeFrom:toAccount: %@"
+ "AAUIMainSettingsViewController dealloc"
+ "AAUIMainSettingsViewController missing reference for AADeviceLocatorStateDidChangeNotification"
+ "AAUIMainSettingsViewController observed AADeviceLocatorStateDidChangeNotification"
+ "AAUIiCloudViewController - setting account manager"
+ "AAUIiCloudViewController: ADP state changed, reloading specifier"
+ "AAUIiCloudViewController: Received notification: %@"
+ "AAUIiCloudViewController: adding CDP Web specifier"
+ "AAUIiCloudViewController: adding CDP specifier"
+ "AAUIiCloudViewController: cached state: %d, fetched state: %d"
+ "AAUIiCloudViewController: fetched ADP state in background: %d"
+ "AAUIiCloudViewController: fetching ADP state in background"
+ "H:|-%f-[_deviceImageView]-%f-|"
+ "H:|-%f-[_deviceNameLabel]-%f-|"
+ "H:|-%f-[detail]-%f-|"
+ "Private email specifier tapped, url %@"
+ "V:|-%f-[_deviceImageView(==%f)]-%f-[_deviceNameLabel][detail]-%f-|"
+ "[AAUIAppleAccountViewController _layoutIdentityCardHeader]: was called."
+ "[AAUIAppleAccountViewController _layoutTableHeaderView]: was called."
+ "[AAUIAppleAccountViewController _setupAppleAccountHeader]: was called."
+ "[AAUIAppleAccountViewController _setupIdentityCardHeader]: Reloading specifiers."
+ "[AAUIAppleAccountViewController _setupIdentityCardHeader]: deallocated, skipping header view setup."
+ "[AAUIAppleAccountViewController _setupIdentityCardHeader]: fetched Me Card."
+ "[AAUIAppleAccountViewController _setupIdentityCardHeader]: layout identity card."
+ "[AAUIAppleAccountViewController _setupIdentityCardHeader]: was called."
+ "_cleanupADPSpecifiers"
+ "_cropRectForRawImageOrientation:"
+ "alertWithTitle:message:"
+ "currentQueue"
+ "imageOrientation"
+ "imageWithCIImage:scale:orientation:"
+ "setADPState:"
+ "settingsToggleSignOut"
+ "updating the specifiers in the iCloudVC"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "\x02\x12\x11\x11"
- "\x0f\x03"
- "!A"
- "%@: Controller (%@) did receieve objectModel (%@) with actionSignal (%lu)"
- "%@: Undefined action signal and no page, not displaying modally! Processing objectModel (%@) with handler (%@)"
- "AADataclassConfigurationViewController dealloc %@"
- "AAUIAppleAccountViewController dealloc %@"
- "AAUIAppleAccountViewController fetched Me Card"
- "AAUIAppleAccountViewController layout identity card"
- "AAUICDPSpecifierProvider: ADP state changed, reloading specifier"
- "AAUICDPSpecifierProvider: Received notification: %@"
- "AAUICDPSpecifierProvider: dealloc called."
- "AAUICDPSpecifierProvider: fetched ADP state in background: %d"
- "AAUICDPSpecifierProvider: fetching ADP state in background"
- "H:|-%d-[_deviceImageView]-%d-|"
- "H:|-%d-[_deviceNameLabel]-%d-|"
- "H:|-%d-[detail]-%d-|"
- "Observed AADeviceLocatorStateDidChangeNotification for strongSelf %@"
- "V:|-%d-[_deviceImageView(==%d)]-%d-[_deviceNameLabel][detail]-%d-|"
- "_accountDidChangeFrom:toAccount: %@"
- "alertControllerWithTitle:message:preferredStyle:"
- "backup.png"
- "footerLabelTextColor"
- "imageWithCIImage:"
- "private email specifier tapped, url %@"

```
