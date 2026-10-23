(() => {
  const nodes = [...document.querySelectorAll('.mermaid')];
  if (!nodes.length || !window.mermaid) return;
  const originals = nodes.map(node => node.textContent);
  let rendering = Promise.resolve();
  function render() {
    rendering = rendering.then(async () => {
      mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: document.documentElement.dataset.theme === 'dark' ? 'dark' : 'neutral', fontFamily: '"PingFang SC", "Microsoft YaHei", sans-serif' });
      nodes.forEach((node, index) => { node.removeAttribute('data-processed'); node.textContent = originals[index]; });
      await mermaid.run({ nodes });
    }).catch(error => console.error('Diagram rendering failed', error));
  }
  render();
  new MutationObserver(render).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
})();
