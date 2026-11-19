## Sharing

> `/System/Library/ExtensionKit/Extensions/Sharing.appex/Contents/MacOS/Sharing`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-2027.0.3.0.0
-  __TEXT.__text: 0x12b780
-  __TEXT.__auth_stubs: 0x3380
-  __TEXT.__objc_stubs: 0xb520
-  __TEXT.__objc_methlist: 0x4ffc
-  __TEXT.__objc_methname: 0xfc9d
-  __TEXT.__cstring: 0x669e
+2027.1.2.0.0
+  __TEXT.__text: 0x12c8d8
+  __TEXT.__auth_stubs: 0x3390
+  __TEXT.__objc_stubs: 0xb5c0
+  __TEXT.__objc_methlist: 0x5034
+  __TEXT.__objc_methname: 0xfd1d
+  __TEXT.__cstring: 0x66fe
   __TEXT.__objc_classname: 0xaed
   __TEXT.__objc_methtype: 0x216a
-  __TEXT.__const: 0x7d6c
+  __TEXT.__const: 0x7d8c
   __TEXT.__gcc_except_tab: 0x2a4
-  __TEXT.__oslogstring: 0x465
-  __TEXT.__swift5_typeref: 0x1817c
+  __TEXT.__oslogstring: 0x615
+  __TEXT.__swift5_typeref: 0x181ae
   __TEXT.__constg_swiftt: 0x4168
   __TEXT.__swift5_reflstr: 0x2120
   __TEXT.__swift5_fieldmd: 0x17dc

   __TEXT.__swift_as_cont: 0x328
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x4678
+  __TEXT.__unwind_info: 0x46b8
   __TEXT.__eh_frame: 0x2c04
   __DATA_CONST.__const: 0x6ab8
-  __DATA_CONST.__cfstring: 0x4380
+  __DATA_CONST.__cfstring: 0x43a0
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x138
-  __DATA_CONST.__auth_got: 0x19d0
-  __DATA_CONST.__got: 0xe40
+  __DATA_CONST.__auth_got: 0x19d8
+  __DATA_CONST.__got: 0xe90
   __DATA_CONST.__auth_ptr: 0xbf8
-  __DATA.__objc_const: 0xa130
-  __DATA.__objc_selrefs: 0x3a08
+  __DATA.__objc_const: 0xa138
+  __DATA.__objc_selrefs: 0x3a38
   __DATA.__objc_ivar: 0x6e4
   __DATA.__objc_data: 0x6970
-  __DATA.__data: 0x6a68
+  __DATA.__data: 0x6b68
   __DATA.__bss: 0x3df8
   __DATA.__common: 0x2a8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5815
-  Symbols:   1010
-  CStrings:  3980
+  Functions: 5832
+  Symbols:   1011
+  CStrings:  3992
 
Symbols:
+ __kACSMSettingsCurrentDDMConfigKey
CStrings:
+ "%{public}@: ddm=%{BOOL}d settings=%{BOOL}d managedPref=%{BOOL}d -> %{BOOL}d"
+ "(none)"
+ "CCService.shared() unavailable in extension"
+ "CPProfilePreferencesChangedNotification fired, isManaged=%{BOOL}d"
+ "Content Caching managed: cc="
+ "currentDDMConfig"
+ "isActivationOverriddenForKey:"
+ "isDDMManaged"
+ "isMainThread"
+ "isManaged KVO -> %{BOOL}d main=%{BOOL}d sheetOpen=%{BOOL}d"
+ "manager:didStartAbsorbingCache:withError:"
+ "serviceIsManagedByProfile"
+ "setSettings: DDM %{public}@ -> %{public}@ announce=%{BOOL}d isManaged=%{BOOL}d main=%{BOOL}d"
+ "settingsValueForKey %{public}@: source=disk needDeepState=%{BOOL}d value=%{public}@ class=%{public}@"
+ "settingsValueForKey %{public}@: source=settings value=%{public}@ class=%{public}@"
+ "settingsValueForKey:"
- "AutoActivation"
- "AutoActivation is active"
- "DenyActivation"
- "DenyActivation is active"
```
