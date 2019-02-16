function FindProxyForURL(url, host) {
    if (host=='www.example.com') {
        return 'PROXY 127.0.0.1:8000';
    }
    else if (host=='www.prototype.com') {
        return 'PROXY 127.0.0.1:8000';       
    }
    return 'DIRECT';
}
