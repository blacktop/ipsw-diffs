## BlissReader

> `/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-6647.0.0.0.0
-  __TEXT.__text: 0x2a3a3c
+6655.0.0.0.0
+  __TEXT.__text: 0x2a4890
   __TEXT.__auth_stubs: 0x2ef0
-  __TEXT.__objc_stubs: 0x60780
+  __TEXT.__objc_stubs: 0x60960
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x498cc
-  __TEXT.__const: 0xbe10
-  __TEXT.__gcc_except_tab: 0x5b50
-  __TEXT.__cstring: 0x36a16
-  __TEXT.__objc_methname: 0x8e157
+  __TEXT.__objc_methlist: 0x49984
+  __TEXT.__const: 0xbe40
+  __TEXT.__gcc_except_tab: 0x5bf4
+  __TEXT.__cstring: 0x36a66
+  __TEXT.__objc_methname: 0x8e3b3
   __TEXT.__objc_classname: 0xd784
   __TEXT.__objc_methtype: 0x1f236
-  __TEXT.__oslogstring: 0xc0e
+  __TEXT.__oslogstring: 0xe42
   __TEXT.__ustring: 0x3c0
-  __TEXT.__swift5_typeref: 0xaf
-  __TEXT.__swift5_capture: 0x8c
+  __TEXT.__swift5_typeref: 0x93
+  __TEXT.__swift5_capture: 0x88
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x4
-  __TEXT.__unwind_info: 0xdf20
+  __TEXT.__unwind_info: 0xdf70
   __TEXT.__eh_frame: 0xb0
-  __DATA_CONST.__const: 0x15fc8
-  __DATA_CONST.__cfstring: 0x26ac0
+  __DATA_CONST.__const: 0x16018
+  __DATA_CONST.__cfstring: 0x26b20
   __DATA_CONST.__objc_classlist: 0x2f88
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0xc40

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__auth_got: 0x1790
-  __DATA_CONST.__got: 0x1c00
+  __DATA_CONST.__got: 0x1c10
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x7cb20
-  __DATA.__objc_selrefs: 0x1ed88
-  __DATA.__objc_ivar: 0x3e48
+  __DATA.__objc_const: 0x7cbb0
+  __DATA.__objc_selrefs: 0x1ee20
+  __DATA.__objc_ivar: 0x3e54
   __DATA.__objc_data: 0x1db50
   __DATA.__data: 0xa880
   __DATA.__bss: 0x8fc

   - @rpath/BookAnalytics.framework/BookAnalytics
   - @rpath/BookCore.framework/BookCore
   - @rpath/BookEPUB.framework/BookEPUB
-  Functions: 22731
-  Symbols:   7554
-  CStrings:  32253
+  Functions: 22749
+  Symbols:   7556
+  CStrings:  32289
 
Symbols:
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_UIDeferredMenuElement
+ _swift_release_x23
- _swift_release_x25
CStrings:
+ "@\"UIMenu\"16@?0@\"UIMenu\"8"
+ "Menu"
+ "MenuButton"
+ "T@\"UIBarButtonItem\",&,N,V_readerMenuButtonItem"
+ "T@\"UIView\",&,N,V_emptyInputView"
+ "TB,N,V_readerMenuPresented"
+ "[DRMTrace][open] -> silent keybag refetch dsid=%{private}@ connected=%{BOOL}d"
+ "[DRMTrace][open] Auth needed due to non-existing account for asset at url, username: %@ -- %@"
+ "[DRMTrace][open] Error authenticating account: %@ -- %@"
+ "[DRMTrace][open] Error refetching bag for dsid: %@ -- %@"
+ "[DRMTrace][open] bliss DRM validate failed; domain=%{public}@ code=%ld"
+ "[DRMTrace][open] bliss identity: usernamePresent=%{BOOL}d dsid=%{private}@"
+ "[DRMTrace][open] bliss interactive auth result ok=%{BOOL}d err=%{public}@"
+ "[DRMTrace][open] bliss open failed err=%{public}@ underlying=%{public}@ refetchRequired=%{BOOL}d canRefetch=%{BOOL}d"
+ "[DRMTrace][open] gate(bliss): accountNil=%{BOOL}d credentialEmpty=%{BOOL}d credential=%{private}@"
+ "_contextMenuInteraction"
+ "_emptyInputView"
+ "_readerMenuButtonItem"
+ "_readerMenuPresented"
+ "_scrubberFrameHorizontalOriginY"
+ "contentInsetSafeAreaEdgesToSubtract"
+ "elementWithUncachedProvider:"
+ "ellipsis"
+ "emptyInputView"
+ "footerToolbarHeight"
+ "initWithImage:style:target:action:"
+ "menuRepresentation"
+ "menuWithTitle:children:"
+ "p_buildReaderMenu"
+ "p_readerMenuActuallyVisible"
+ "p_readerMenuChildren"
+ "p_readerMenuElementForBarButtonItem:"
+ "readerMenuButtonItem"
+ "readerMenuPresented"
+ "scrubberHeight"
+ "setEmptyInputView:"
+ "setMenu:"
+ "setReaderMenuButtonItem:"
+ "setReaderMenuPresented:"
+ "updateVisibleMenuWithBlock:"
+ "v16@?0@?<v@?@\"NSArray\">8"
- "Auth needed due to non-existing account for asset at url, username: %@ -- %@"
- "Error authenticating account: %@ -- %@"
- "Error refetching bag for dsid: %@ -- %@"
- "assetViewControllerMinifiedBarButtonItem:"
- "leftBarButtonItem"
```
