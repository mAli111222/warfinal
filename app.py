from flask import Flask, render_template, request, redirect, url_for

@app.route('/', methods=['GET'])
def home():


      word = '''

VG8gcHJlcGFyZSBmb3IgdGhpcyBjb3Vyc2UsIEkgc3RhcnRlZCDigJxUaGUgY29tcGxldGUgZXRoaWNhbCBoYWNraW5nIGNvdXJzZSBieSBBdGlsIFNhbWFuY2lvZ2x14oCdIG9uIFVkZW15LiBJIGJvdWdodCB0aGlzIDEgeWVhciBhZ28sIGFuZCBJIGFtIGRvaW5nIGl0IGF0IG15IG93biBwYWNlLCBhbG9uZyB3aXRoIG15IEEgbGV2ZWxzLCB0byBicm9hZGVuIG15IGtub3dsZWRnZSBhbmQgc2tpbGwgaW4gdGhpcyB0b3BpYy4gQWxzbywgSSBoYXZlIGp1c3Qgc3RhcnRlZCBhIGNvdXJzZSBvbiBUcnlIYWNrTWUuIE15IGdvYWwgZm9yIG1pZC0yMDIxIGlzIHRvIGNvbXBsZXRlIGF0IGxlYXN0IDEgcGF0aC4gRG9pbmcgdGhpcyB3aWxsIGVuc3VyZSB0aGF0IEkgd2lsbCBiZSBvbiBwYXIgd2l0aCBteSBwZWVycyBhdCB1bml2ZXJzaXR5LCB3aG9tIEkgcHJlc3VtZSB3aWxsIGFsc28gaGF2ZSBnb29kIGtub3dsZWRnZSBvbiB0aGlzIHRvcGljIHJpZ2h0IG9mZiB0aGUgYmF0LiBJIGFsc28gbG9vayBmb3J3YXJkIHRvIG1lZXRpbmcgZXhjZXB0aW9uYWwgcGVlcnMgaW4gV2Fyd2ljay4gSSBiZWxpZXZlIHRoZXNlIHBlb3BsZSwgYXMgd2VsbCBhcyB0aGUgbGVjdHVyZXJzLCB3aWxsIG9wZW4gbXkgZXllcyB0byBwcm9ibGVtLXNvbHZpbmcgb24gYSBsZXZlbCBJIHdvdWxkIG5ldmVyIGV2ZW4gdGhpbmsgb2YuIFdoYXQgSSB3aWxsIHJldHVybiBpcyBteSBhYmlsaXR5IHRvIHRoaW5rIG91dHNpZGUgdGhlIGJveDsgY3JlYXRpdml0eTsgY29tbXVuaWNhdGlvbiBza2lsbHM7IHRoZSBhYmlsaXR5IHRvIHRoaW5rIG9mIG11bHRpcGxlIHNvbHV0aW9ucyB0byBhIHByb2JsZW0gKG1pbmQgc29tZXRpbWVzIEkgZG8gbm90IHBvc3Nlc3MgdGhlIGZ1bGwga25vd2xlZGdlIG9uIGhvdyB0byBzb2x2ZSB0aGVzZSBwcm9ibGVtcykgYW5kIHdvcmtpbmcgd2VsbCBib3RoIGluIGEgdGVhbSBhbmQgYnkgbXlzZWxmLg0KSSBoYXZlIGFsc28gbWFkZSBjb25uZWN0aW9ucyBvbiBMaW5rZWRJbiB3aXRoIEN5YmVyc2VjdXJpdHkgcHJvZmVzc2lvbmFscyBhbmQgam9pbmVkIGZvcnVtcyB0byBoYXZlIGVzdGFibGlzaGVkIGNvbm5lY3Rpb25zIHdpdGggcGVvcGxlIGluIHRoZSBpbmR1c3RyeS4gSXQgd2lsbCBhbHNvIGFsbG93IG1lIHRvIG1ha2UgbW9yZSBjb25uZWN0aW9ucyBhbmQgcG90ZW50aWFsbHkgZ2V0IG1lIGhpcmVkIG9uY2UgSSBsZWF2ZSB1bml2ZXJzaXR5LiANCkZpbmFsbHksIEkgb25seSByZWNlbnRseSBwcmludGVkIGFydGljbGVzIG9uIG15IHdhbGwgdG8gcmVhZCB3aGVuIEkgYW0gYm9yZWQgb3IgcmVzdGluZy4gRXZlbiB0aG91Z2ggSSBtYXkgbm90IHVuZGVyc3RhbmQgd2hhdCBhbGwgdGhlc2UgYXJ0aWNsZXMgbWVhbiBzdWNoIGFzIHdoYXQgYSBXQkFOIGlzLCByZWFkaW5nIGZ1cnRoZXIgb24sIEkgZmluZCBvdXQgdGhhdCBpdCdzIHVzZWQgaW4gaGVhbHRoY2FyZSBzeXN0ZW1zIGFuZCA1Ry4gQnV0IGFsc28sIHRoZSBmYWN0IHRoYXQgdGhlc2Ugc2Vuc29ycyBsYWNrIGFub255bWl0eSwgd2hpY2ggY2FuIGJlIHVzZWQgcG9zc2libHkgZm9yIG1hbGljaW91cyBhdHRhY2tzLiBUaGlzIHNob3dzIG15IGRlc2lyZSBmb3IgbW9yZSBrbm93bGVkZ2UgYW5kIG15IGF0dGl0dWRlIHRvd2FyZHMgdGhpcyBpbmR1c3RyeS4gDQo=




'''

      return word
#I understand this is very sloppy python but it works pretty well and I decided to spend more time with my batch code and pushing this to Azure

@app.route('/cyber2', methods=['GET'])
def c2():
      word = '''

MiBhc3BlY3RzIG9mIHRoaXMgY291cnNlIHRoYXQgSSBiZWxpZXZlIEkgd2lsbCBmaW5kIHRoZSBtb3N0IGNoYWxsZW5naW5nIGlzIGdyYXNwaW5nIGNvbmNlcHRzIHRoZSBmaXJzdCB0aW1lIGFyb3VuZC4gVGhpcyBpcyBiZWNhdXNlLCBJIGJlbGlldmUgdGhhdCB0b3BpY3Mgc3VjaCBhcyDigJxEYXRhIHNjaWVuY2UsIGFsZ29yaXRobXMgYW5kIGNvbXBsZXhpdHkgaW4gdGhlIGN5YmVyIGNvbnRleHTigJ0gYW5kIOKAnGluZm9ybWF0aW9uIG1hbmFnZW1lbnTigJ0gd2lsbCBiZSBoYXJkIHRvIGNvbXBsZXRlbHkgdW5kZXJzdGFuZCBzaW5jZSBpdCBjb250YWlucyBkYXRhYmFzZXMgYW5kIGFsZ29yaXRobXMuIEhvd2V2ZXIsIGtub3dpbmcgdGhhdCBteSBsZWN0dXJlcnMgaW4gV2Fyd2ljayB3aWxsIGhhdmUgbXkgYmVzdCBpbnRlcmVzdCBhdCBoZWFydCwgSSBiZWxpZXZlIHRoZXkgd2lsbCB0YWtlIHRoZSB0aW1lIHRvIGhlbHAgbWUgdW5kZXJzdGFuZCB0aGVzZSBjb25jZXB0cyBhbmQgdGhlcmVmb3JlIGhlbHAgbWUgZnVsZmlsIG15IGRlZ3JlZSBhbmQgY2FyZWVyIGluIHRoZSBpbmR1c3RyeS4NClRoZSBuZXh0IGFzcGVjdCB3aWxsIGJlIG1haW50YWluaW5nIG15IGxldmVsIG9mIGNvbXBldGl0aXZlbmVzcyBhbW9uZ3N0IG15IHBlZXJzLiBJIGFscmVhZHkga25vdyB0aGF0IHRoZXJlIHdpbGwgYmUgc29tZSBwZWVycyB3aG8gd2lsbCBiZSBtdWNoIGJldHRlciB0aGFuIG1lIGluIHRlcm1zIG9mIGtub3dsZWRnZSBhbmQgbG9naWMuIEkgbGlrZSB0byBjb21wZXRlIHdpdGggdGhlc2UgaW5kaXZpZHVhbHMgYmVjYXVzZSBpdCBmdWVscyBteSBtb3RpdmF0aW9uIGFuZCBteSB0aGlyc3QgdG8gaW1wcm92ZSBpbiB0aGUgY291cnNlLiBXaGF0IHdpbGwgYmUgY2hhbGxlbmdpbmcgaXMgbWUgYWNjZXB0aW5nIHRoYXQgSSB3aWxsIG5vdCBiZSBhYmxlIHRvIGFsd2F5cyBvdXRwZXJmb3JtLCBidXQgSSBtdXN0IGtlZXAgdGhhdCBkcml2ZSBhbmQgd29yayB3aXRoIGl0LiAgDQoNCldoYXQgSSBiZWxpZXZlIHdpbGwgYmUgdGhlIG1vc3QgZnVsZmlsbGluZyBpcyBkb2luZyBoYW5kcy1vbiBsZWFybmluZyBzdWNoIGFzIHRoZSBwcm9ncmFtbWluZyBhc3BlY3Qgb2YgdGhlIGNvdXJzZSB3aGVyZSB3ZSB3aWxsIGJlIGxlYXJuaW5nIGhvdyB0byB0YWtlIGFkdmFudGFnZSBvZiBmdW5jdGlvbmFsIGxhbmd1YWdlcyBhbmQgb2JqZWN0LW9yaWVudGF0ZWQgbGFuZ3VhZ2VzLiBJIGxvb2sgZm9yd2FyZCB0byBsZWFybmluZyBob3cgdG8gd3JpdGUgd2l0aCBmdW5jdGlvbmFsIGxhbmd1YWdlcyBzaW5jZSBpdCByZXF1aXJlcyBtdWNoIG1vcmUgbG9naWNhbCB0aGlua2luZywgaG93ZXZlciwgSSBjaG9zZSB0byBmb2N1cyB0aW1lIG9uIGxhbmd1YWdlcyBzdWNoIGFzIFB5dGhvbiwgSmF2YVNjcmlwdCwgYW5kIERhcnQuDQpUaGUgbmV4dCBhc3BlY3QgSSBiZWxpZXZlIHdpbGwgYmUgZnVsZmlsbGluZyBpcyBsZWFybmluZyBhYm91dCBodW1hbiBiZWhhdmlvdXIgaW4gY3liZXJzZWN1cml0eSwgbG9va2luZyBtb3JlIGludG8gdGhlIOKAnGh1bWFuIGZhY3RvcnMgYW5kIHNlY3VyaXR54oCdIG1vZHVsZS4gVGhpcyBpcyBiZWNhdXNlIEkgYW0gdmVyeSBpbnRlcmVzdGVkIGluIHNvY2lhbCBlbmdpbmVlcmluZyBhbmQgSSBiZWxpZXZlIGl0IHdpbGwgYmUgdXNlZnVsIHRvIGxlYXJuIGFib3V0IHNpbmNlIDEpIGl0IHdpbGwgaGVscCB3aXRoIGluZm9ybWF0aW9uIHNlY3VyaXR5IGV4YW1wbGVzIGJlaW5nIGhvdyBzb21lIGhhY2tlcnMgY2FuIGNhbGwgbW9iaWxlIHBob25lIHByb3ZpZGVycyBhbmQgZ2V0IHRoZWlyIHRhcmdldHMgaW5mb3JtYXRpb24gYXMgd2VsbCBhcyBhIHJlcGxhY2VtZW50IHNpbSBjYXJkLCAyKSBJIHdhbnQgbXkgY2FyZWVyIHJvdXRlIHRvIGJlIG1vcmUgZm9jdXNlZCBvbiBwZW5ldHJhdGlvbiB0ZXN0aW5nLCB0aGVyZWZvcmUgaXQgd2lsbCBoZWxwIG1lIHdpdGggZmluZGluZyBodW1hbiBpc3N1ZXMgZm9yIG15IGNsaWVudHMnIGNvbXBhbmllcy4NCg==


'''
      return word
