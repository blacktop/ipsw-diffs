## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-952.10.8.0.0
-  __TEXT.__text: 0x286bc
+952.20.2.0.0
+  __TEXT.__text: 0x28698
   __TEXT.__auth_stubs: 0x930
   __TEXT.__objc_stubs: 0x5460
   __TEXT.__objc_methlist: 0x2684

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x4a8
-  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__got: 0x5a8
   __DATA.__objc_const: 0x4df8
   __DATA.__objc_selrefs: 0x1c90
   __DATA.__objc_ivar: 0x27c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 905
-  Symbols:   2568
+  Symbols:   2567
   CStrings:  1992
 
Symbols:
+ _WLKHTTPStatusCodeForError
- _AMSErrorDomain
- _WLKHTTPStatusCodeForAMSError
Functions:
~ -[WLDPlaybackManager _handleReportingError:forSummary:] : 332 -> 296
```
